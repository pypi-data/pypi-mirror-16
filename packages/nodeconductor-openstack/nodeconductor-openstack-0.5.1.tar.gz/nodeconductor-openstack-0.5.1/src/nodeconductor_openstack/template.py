from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple, AdminTextareaWidget

from rest_framework import serializers

from nodeconductor.core import models as core_models
from nodeconductor.template.forms import ResourceTemplateForm
from nodeconductor.template.serializers import BaseResourceTemplateSerializer

from . import models


class NestedHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    """ Represents object as {'url': <object_url>} """

    def to_internal_value(self, data):
        return super(NestedHyperlinkedRelatedField, self).to_internal_value(data.get('url'))

    def to_representation(self, value):
        return {'url': super(NestedHyperlinkedRelatedField, self).to_representation(value)}


class InstanceProvisionTemplateForm(ResourceTemplateForm):
    service = forms.ModelChoiceField(
        label="OpenStack service", queryset=models.OpenStackService.objects.all(), required=False)
    tenant = forms.ModelChoiceField(
        label="OpenStack tenant", queryset=models.Tenant.objects.all(), required=False)

    flavor = forms.ModelChoiceField(label="Flavor", queryset=models.Flavor.objects.all(), required=False)
    image = forms.ModelChoiceField(label="Image", queryset=models.Image.objects.all(), required=False)
    ssh_public_key = forms.ModelChoiceField(
        label="SSH public key", queryset=core_models.SshPublicKey.objects.all(), required=False)
    data_volume_size = forms.IntegerField(label='Data volume size', required=False)
    system_volume_size = forms.IntegerField(label='System volume size', required=False)
    security_groups = forms.ModelMultipleChoiceField(
        models.SecurityGroup.objects.all().order_by('name'),
        label='Security groups',
        required=False,
        widget=FilteredSelectMultiple(verbose_name='Instance security groups', is_stacked=False))
    user_data = forms.CharField(label='User data', widget=AdminTextareaWidget(), required=False)
    skip_external_ip_assignment = forms.BooleanField(required=False)
    schedule = forms.CharField(
        required=False, help_text='If defined - DR backup schedule will be added to instance after creation')
    retention_time = forms.IntegerField(required=False)
    maximal_number_of_backups = forms.IntegerField(required=False)

    class Meta(ResourceTemplateForm.Meta):
        fields = ResourceTemplateForm.Meta.fields + ('service', 'tenant', 'project', 'flavor', 'image',
                                                     'data_volume_size', 'system_volume_size')

    class Serializer(BaseResourceTemplateSerializer):
        service = serializers.HyperlinkedRelatedField(
            view_name='openstack-detail',
            queryset=models.OpenStackService.objects.all(),
            lookup_field='uuid',
            required=False,
        )
        tenant = serializers.HyperlinkedRelatedField(
            view_name='openstack-tenant-detail',
            queryset=models.Tenant.objects.all(),
            lookup_field='uuid',
            required=False,
        )
        flavor = serializers.HyperlinkedRelatedField(
            view_name='openstack-flavor-detail',
            lookup_field='uuid',
            queryset=models.Flavor.objects.all(),
            required=False,
        )
        image = serializers.HyperlinkedRelatedField(
            view_name='openstack-image-detail',
            lookup_field='uuid',
            queryset=models.Image.objects.all(),
            required=False,
        )
        ssh_public_key = serializers.HyperlinkedRelatedField(
            view_name='sshpublickey-detail',
            lookup_field='uuid',
            queryset=core_models.SshPublicKey.objects.all(),
            required=False,
        )
        data_volume_size = serializers.IntegerField(required=False)
        system_volume_size = serializers.IntegerField(required=False)
        security_groups = serializers.ListField(
            child=NestedHyperlinkedRelatedField(
                view_name='openstack-sgp-detail',
                lookup_field='uuid',
                queryset=models.SecurityGroup.objects.all()),
            required=False,
        )
        user_data = serializers.CharField(required=False)
        skip_external_ip_assignment = serializers.BooleanField(required=False)
        schedule = serializers.CharField(required=False)
        retention_time = serializers.IntegerField(required=False)
        maximal_number_of_backups = serializers.IntegerField(required=False)

    @classmethod
    def get_serializer_class(cls):
        return cls.Serializer

    @classmethod
    def get_model(cls):
        return models.Instance

    @classmethod
    def post_create(cls, template, instance):
        # Execute custom action after instance creation.
        if template.options.get('schedule'):
            models.BackupSchedule.objects.create(
                instance=instance,
                backup_type=models.BackupSchedule.BackupTypes.DR,
                schedule=template.options['schedule'],
                retention_time=template.options.get('retention_time', 0),
                maximal_number_of_backups=template.options.get('maximal_number_of_backups', 1),
                is_active=True,
            )
