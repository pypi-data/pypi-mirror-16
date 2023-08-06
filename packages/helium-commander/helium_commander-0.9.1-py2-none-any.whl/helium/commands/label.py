import helium
import click
import dpath.util as dpath
from .timeseries import options as timeseries_options
from .timeseries import dump as timeseries_dump
from .sensor import list as sensor_list, sort_option as sensor_sort_option
from .util import tabulate, lookup_resource_id, shorten_json_id, sort_option


pass_service = click.make_pass_decorator(helium.Service)


@click.group()
def cli():
    """Operations on labels of sensors.
    """
    pass


def _tabulate(result, **kwargs):
    def _map_sensor_count(json):
        return len(dpath.get(json, 'relationships/sensor/data'))
    tabulate(result, [
        ('id', shorten_json_id),
        ('sensors', _map_sensor_count),
        ('name', 'attributes/name')
    ], **kwargs)


def _update_label_sensors(ctx, label, sensor, set_func):
    service = ctx.find_object(helium.Service)
    label = lookup_resource_id(service.get_labels, label)
    # Fetch the existing sensors
    sensors = service.get_label_sensors(label).get('data')
    sensor_ids = dpath.values(sensors, "*/id")
    # Look up full sensor ids for all given sensors
    sensor_list = [lookup_resource_id(service.get_sensors, sensor_id)
                   for sensor_id in sensor]
    # And perform the set operation and ensure we have a valid list
    sensor_ids = set_func(set(sensor_ids), set(sensor_list))
    if sensor_ids is None:
        sensor_ids = []
    service.update_label_sensors(label, sensor_ids)


@cli.command()
@click.argument('label', required=False)
@sensor_sort_option
@click.pass_context
def list(ctx, label, **kwargs):
    """Lists information on labels.

    Lists information on a given label or all labels in the organization
    """
    if label:
        ctx.invoke(sensor_list, label=label, **kwargs)
    else:
        service = ctx.find_object(helium.Service)
        _tabulate(service.get_labels(include='sensor').get('data'), **kwargs)


@cli.command()
@click.argument('name', nargs=1)
@click.argument('sensor', nargs=-1)
@click.pass_context
def create(ctx, name, sensor):
    """Create a label.

    Creates a label with a given NAME and an (optional) list of SENSORs
    associated with that label.
    """
    service = ctx.find_object(helium.Service)
    label = service.create_label(name).get('data')
    label_id = label['id']
    if sensor:
        sensor_list = service.get_sensors().get('data')
        sensors = [lookup_resource_id(sensor_list, sensor_id)
                   for sensor_id in sensor]
        service.update_label_sensors(label_id, sensors)
    _tabulate([service.get_label(label_id, include='sensor').get('data')])


@cli.command()
@click.argument('label', nargs=-1)
@pass_service
def delete(service, label):
    """Delete a label.

    Deletes the LABEL with the given id
    """
    label_list = service.get_labels().get('data')
    label = [lookup_resource_id(label_list, label_id)
             for label_id in label]
    for entry in label:
        result = service.delete_label(entry)
        click.echo("Deleted: " + entry
                   if result.status_code == 204 else result)


@cli.command()
@click.argument('label', nargs=1)
@click.argument('sensor', nargs=-1)
@click.pass_context
def add(ctx, label, sensor):
    """Add sensors to a label.

    Adds a given list of SENSORs to the LABEL with the given id.
    """
    _update_label_sensors(ctx, label, sensor, set.union)
    ctx.invoke(sensor_list, label=label)


@cli.command()
@click.argument('label', nargs=1)
@click.argument('sensor', nargs=-1)
@click.pass_context
def remove(ctx, label, sensor):
    """Remove sensors from a label.

    Removes a given list of SENSORs from the LABEL with the given id.
    """
    _update_label_sensors(ctx, label, sensor, set.difference)
    ctx.invoke(sensor_list, label=label)


@cli.command()
@click.argument('label')
@timeseries_options()
@pass_service
def dump(service, label, **kwargs):
    """Dumps timeseries data to files.

    Dumps the timeseries data for all sensors in a given LABEL.

    One file is generated for each sensor with the sensor id as
    filename and the file extension based on the requested dump format

    """
    label = lookup_resource_id(service.get_labels, label)
    sensors = dpath.values(service.get_label_sensors(label), '/data/*/id')
    timeseries_dump(service, sensors, **kwargs)
