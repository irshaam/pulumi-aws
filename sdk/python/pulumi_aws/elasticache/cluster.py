# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    apply_immediately: pulumi.Output[bool]
    """
    Specifies whether any database modifications
    are applied immediately, or during the next maintenance window. Default is
    `false`. See [Amazon ElastiCache Documentation for more information.][1]
    (Available since v0.6.0)
    """
    availability_zone: pulumi.Output[str]
    """
    The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
    """
    az_mode: pulumi.Output[str]
    """
    Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
    """
    cache_nodes: pulumi.Output[list]
    """
    List of node objects including `id`, `address`, `port` and `availability_zone`.
    Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
    """
    cluster_address: pulumi.Output[str]
    """
    (Memcached only) The DNS name of the cache cluster without the port appended.
    """
    cluster_id: pulumi.Output[str]
    """
    Group identifier. ElastiCache converts
    this name to lowercase
    """
    configuration_endpoint: pulumi.Output[str]
    """
    (Memcached only) The configuration endpoint to allow host discovery.
    """
    engine: pulumi.Output[str]
    """
    Name of the cache engine to be used for this cache cluster.
    Valid values for this parameter are `memcached` or `redis`
    """
    engine_version: pulumi.Output[str]
    """
    Version number of the cache engine to be used.
    See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
    in the AWS Documentation center for supported versions
    """
    maintenance_window: pulumi.Output[str]
    """
    Specifies the weekly time range for when maintenance
    on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
    The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
    """
    node_type: pulumi.Output[str]
    """
    The compute and memory capacity of the nodes. See
    [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
    supported node types
    """
    notification_topic_arn: pulumi.Output[str]
    """
    An Amazon Resource Name (ARN) of an
    SNS topic to send ElastiCache notifications to. Example:
    `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
    """
    num_cache_nodes: pulumi.Output[float]
    """
    The initial number of cache nodes that the
    cache cluster will have. For Redis, this value must be 1. For Memcache, this
    value must be between 1 and 20. If this number is reduced on subsequent runs,
    the highest numbered nodes will be removed.
    """
    parameter_group_name: pulumi.Output[str]
    """
    Name of the parameter group to associate
    with this cache cluster
    """
    port: pulumi.Output[float]
    """
    The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
    """
    preferred_availability_zones: pulumi.Output[list]
    """
    A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
    """
    replication_group_id: pulumi.Output[str]
    """
    The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
    """
    security_group_ids: pulumi.Output[list]
    """
    One or more VPC security groups associated
    with the cache cluster
    """
    security_group_names: pulumi.Output[list]
    """
    List of security group
    names to associate with this cache cluster
    """
    snapshot_arns: pulumi.Output[list]
    """
    A single-element string list containing an
    Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
    Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
    """
    snapshot_name: pulumi.Output[str]
    """
    The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
    """
    snapshot_retention_limit: pulumi.Output[float]
    """
    The number of days for which ElastiCache will
    retain automatic cache cluster snapshots before deleting them. For example, if you set
    SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
    before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
    Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
    """
    snapshot_window: pulumi.Output[str]
    """
    The daily time range (in UTC) during which ElastiCache will
    begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
    """
    subnet_group_name: pulumi.Output[str]
    """
    Name of the subnet group to be used
    for the cache cluster.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource
    """
    def __init__(__self__, resource_name, opts=None, apply_immediately=None, availability_zone=None, az_mode=None, cluster_id=None, engine=None, engine_version=None, maintenance_window=None, node_type=None, notification_topic_arn=None, num_cache_nodes=None, parameter_group_name=None, port=None, preferred_availability_zones=None, replication_group_id=None, security_group_ids=None, security_group_names=None, snapshot_arns=None, snapshot_name=None, snapshot_retention_limit=None, snapshot_window=None, subnet_group_name=None, tags=None, __name__=None, __opts__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any database modifications
               are applied immediately, or during the next maintenance window. Default is
               `false`. See [Amazon ElastiCache Documentation for more information.][1]
               (Available since v0.6.0)
        :param pulumi.Input[str] availability_zone: The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        :param pulumi.Input[str] az_mode: Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
        :param pulumi.Input[str] cluster_id: Group identifier. ElastiCache converts
               this name to lowercase
        :param pulumi.Input[str] engine: Name of the cache engine to be used for this cache cluster.
               Valid values for this parameter are `memcached` or `redis`
        :param pulumi.Input[str] engine_version: Version number of the cache engine to be used.
               See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
               in the AWS Documentation center for supported versions
        :param pulumi.Input[str] maintenance_window: Specifies the weekly time range for when maintenance
               on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
               The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
        :param pulumi.Input[str] node_type: The compute and memory capacity of the nodes. See
               [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
               supported node types
        :param pulumi.Input[str] notification_topic_arn: An Amazon Resource Name (ARN) of an
               SNS topic to send ElastiCache notifications to. Example:
               `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
        :param pulumi.Input[float] num_cache_nodes: The initial number of cache nodes that the
               cache cluster will have. For Redis, this value must be 1. For Memcache, this
               value must be between 1 and 20. If this number is reduced on subsequent runs,
               the highest numbered nodes will be removed.
        :param pulumi.Input[str] parameter_group_name: Name of the parameter group to associate
               with this cache cluster
        :param pulumi.Input[float] port: The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        :param pulumi.Input[list] preferred_availability_zones: A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
        :param pulumi.Input[str] replication_group_id: The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
        :param pulumi.Input[list] security_group_ids: One or more VPC security groups associated
               with the cache cluster
        :param pulumi.Input[list] security_group_names: List of security group
               names to associate with this cache cluster
        :param pulumi.Input[list] snapshot_arns: A single-element string list containing an
               Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
               Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        :param pulumi.Input[str] snapshot_name: The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
        :param pulumi.Input[float] snapshot_retention_limit: The number of days for which ElastiCache will
               retain automatic cache cluster snapshots before deleting them. For example, if you set
               SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
               before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
               Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
        :param pulumi.Input[str] snapshot_window: The daily time range (in UTC) during which ElastiCache will
               begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
        :param pulumi.Input[str] subnet_group_name: Name of the subnet group to be used
               for the cache cluster.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticache_cluster.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apply_immediately'] = apply_immediately

        __props__['availability_zone'] = availability_zone

        __props__['az_mode'] = az_mode

        __props__['cluster_id'] = cluster_id

        __props__['engine'] = engine

        __props__['engine_version'] = engine_version

        __props__['maintenance_window'] = maintenance_window

        __props__['node_type'] = node_type

        __props__['notification_topic_arn'] = notification_topic_arn

        __props__['num_cache_nodes'] = num_cache_nodes

        __props__['parameter_group_name'] = parameter_group_name

        __props__['port'] = port

        __props__['preferred_availability_zones'] = preferred_availability_zones

        __props__['replication_group_id'] = replication_group_id

        __props__['security_group_ids'] = security_group_ids

        __props__['security_group_names'] = security_group_names

        __props__['snapshot_arns'] = snapshot_arns

        __props__['snapshot_name'] = snapshot_name

        __props__['snapshot_retention_limit'] = snapshot_retention_limit

        __props__['snapshot_window'] = snapshot_window

        __props__['subnet_group_name'] = subnet_group_name

        __props__['tags'] = tags

        __props__['cache_nodes'] = None
        __props__['cluster_address'] = None
        __props__['configuration_endpoint'] = None

        super(Cluster, __self__).__init__(
            'aws:elasticache/cluster:Cluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

