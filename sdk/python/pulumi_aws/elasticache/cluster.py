# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 az_mode: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[str]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 notification_topic_arn: Optional[pulumi.Input[str]] = None,
                 num_cache_nodes: Optional[pulumi.Input[int]] = None,
                 parameter_group_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 preferred_availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 replication_group_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
                 snapshot_retention_limit: Optional[pulumi.Input[int]] = None,
                 snapshot_window: Optional[pulumi.Input[str]] = None,
                 subnet_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
        For working with Redis (Cluster Mode Enabled) replication groups, see the
        `elasticache.ReplicationGroup` resource.

        > **Note:** When you change an attribute, such as `node_type`, by default
        it is applied in the next maintenance window. Because of this, this provider may report
        a difference in its planning phase because the actual modification has not yet taken
        place. You can use the `apply_immediately` flag to instruct the service to apply the
        change immediately. Using `apply_immediately` can result in a brief downtime as the server reboots.
        See the AWS Docs on [Modifying an ElastiCache Cache Cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Modify.html) for more information.

        ## Example Usage
        ### Memcached Cluster

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticache.Cluster("example",
            engine="memcached",
            node_type="cache.m4.large",
            num_cache_nodes=2,
            parameter_group_name="default.memcached1.4",
            port=11211)
        ```
        ### Redis Instance

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticache.Cluster("example",
            engine="redis",
            engine_version="3.2.10",
            node_type="cache.m4.large",
            num_cache_nodes=1,
            parameter_group_name="default.redis3.2",
            port=6379)
        ```
        ### Redis Cluster Mode Disabled Read Replica Instance

        These inherit their settings from the replication group.

        ```python
        import pulumi
        import pulumi_aws as aws

        replica = aws.elasticache.Cluster("replica", replication_group_id=aws_elasticache_replication_group["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any database modifications
               are applied immediately, or during the next maintenance window. Default is
               `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
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
        :param pulumi.Input[int] num_cache_nodes: The initial number of cache nodes that the
               cache cluster will have. For Redis, this value must be 1. For Memcache, this
               value must be between 1 and 20. If this number is reduced on subsequent runs,
               the highest numbered nodes will be removed.
        :param pulumi.Input[str] parameter_group_name: Name of the parameter group to associate
               with this cache cluster
        :param pulumi.Input[int] port: The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preferred_availability_zones: A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
        :param pulumi.Input[str] replication_group_id: The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: One or more VPC security groups associated
               with the cache cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_names: List of security group
               names to associate with this cache cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] snapshot_arns: A single-element string list containing an
               Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
               Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        :param pulumi.Input[str] snapshot_name: The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
        :param pulumi.Input[int] snapshot_retention_limit: The number of days for which ElastiCache will
               retain automatic cache cluster snapshots before deleting them. For example, if you set
               SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
               before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
               Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
        :param pulumi.Input[str] snapshot_window: The daily time range (in UTC) during which ElastiCache will
               begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
        :param pulumi.Input[str] subnet_group_name: Name of the subnet group to be used
               for the cache cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
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
            __props__['arn'] = None
            __props__['cache_nodes'] = None
            __props__['cluster_address'] = None
            __props__['configuration_endpoint'] = None
        super(Cluster, __self__).__init__(
            'aws:elasticache/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            apply_immediately: Optional[pulumi.Input[bool]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            az_mode: Optional[pulumi.Input[str]] = None,
            cache_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterCacheNodeArgs']]]]] = None,
            cluster_address: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            configuration_endpoint: Optional[pulumi.Input[str]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            maintenance_window: Optional[pulumi.Input[str]] = None,
            node_type: Optional[pulumi.Input[str]] = None,
            notification_topic_arn: Optional[pulumi.Input[str]] = None,
            num_cache_nodes: Optional[pulumi.Input[int]] = None,
            parameter_group_name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            preferred_availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            replication_group_id: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            snapshot_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            snapshot_name: Optional[pulumi.Input[str]] = None,
            snapshot_retention_limit: Optional[pulumi.Input[int]] = None,
            snapshot_window: Optional[pulumi.Input[str]] = None,
            subnet_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any database modifications
               are applied immediately, or during the next maintenance window. Default is
               `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
               (Available since v0.6.0)
        :param pulumi.Input[str] availability_zone: The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        :param pulumi.Input[str] az_mode: Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterCacheNodeArgs']]]] cache_nodes: List of node objects including `id`, `address`, `port` and `availability_zone`.
               Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
        :param pulumi.Input[str] cluster_address: (Memcached only) The DNS name of the cache cluster without the port appended.
        :param pulumi.Input[str] cluster_id: Group identifier. ElastiCache converts
               this name to lowercase
        :param pulumi.Input[str] configuration_endpoint: (Memcached only) The configuration endpoint to allow host discovery.
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
        :param pulumi.Input[int] num_cache_nodes: The initial number of cache nodes that the
               cache cluster will have. For Redis, this value must be 1. For Memcache, this
               value must be between 1 and 20. If this number is reduced on subsequent runs,
               the highest numbered nodes will be removed.
        :param pulumi.Input[str] parameter_group_name: Name of the parameter group to associate
               with this cache cluster
        :param pulumi.Input[int] port: The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preferred_availability_zones: A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
        :param pulumi.Input[str] replication_group_id: The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: One or more VPC security groups associated
               with the cache cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_names: List of security group
               names to associate with this cache cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] snapshot_arns: A single-element string list containing an
               Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
               Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        :param pulumi.Input[str] snapshot_name: The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
        :param pulumi.Input[int] snapshot_retention_limit: The number of days for which ElastiCache will
               retain automatic cache cluster snapshots before deleting them. For example, if you set
               SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
               before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
               Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
        :param pulumi.Input[str] snapshot_window: The daily time range (in UTC) during which ElastiCache will
               begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
        :param pulumi.Input[str] subnet_group_name: Name of the subnet group to be used
               for the cache cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["apply_immediately"] = apply_immediately
        __props__["arn"] = arn
        __props__["availability_zone"] = availability_zone
        __props__["az_mode"] = az_mode
        __props__["cache_nodes"] = cache_nodes
        __props__["cluster_address"] = cluster_address
        __props__["cluster_id"] = cluster_id
        __props__["configuration_endpoint"] = configuration_endpoint
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["maintenance_window"] = maintenance_window
        __props__["node_type"] = node_type
        __props__["notification_topic_arn"] = notification_topic_arn
        __props__["num_cache_nodes"] = num_cache_nodes
        __props__["parameter_group_name"] = parameter_group_name
        __props__["port"] = port
        __props__["preferred_availability_zones"] = preferred_availability_zones
        __props__["replication_group_id"] = replication_group_id
        __props__["security_group_ids"] = security_group_ids
        __props__["security_group_names"] = security_group_names
        __props__["snapshot_arns"] = snapshot_arns
        __props__["snapshot_name"] = snapshot_name
        __props__["snapshot_retention_limit"] = snapshot_retention_limit
        __props__["snapshot_window"] = snapshot_window
        __props__["subnet_group_name"] = subnet_group_name
        __props__["tags"] = tags
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[bool]:
        """
        Specifies whether any database modifications
        are applied immediately, or during the next maintenance window. Default is
        `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
        (Available since v0.6.0)
        """
        return pulumi.get(self, "apply_immediately")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> pulumi.Output[str]:
        """
        Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
        """
        return pulumi.get(self, "az_mode")

    @property
    @pulumi.getter(name="cacheNodes")
    def cache_nodes(self) -> pulumi.Output[Sequence['outputs.ClusterCacheNode']]:
        """
        List of node objects including `id`, `address`, `port` and `availability_zone`.
        Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
        """
        return pulumi.get(self, "cache_nodes")

    @property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> pulumi.Output[str]:
        """
        (Memcached only) The DNS name of the cache cluster without the port appended.
        """
        return pulumi.get(self, "cluster_address")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        Group identifier. ElastiCache converts
        this name to lowercase
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> pulumi.Output[str]:
        """
        (Memcached only) The configuration endpoint to allow host discovery.
        """
        return pulumi.get(self, "configuration_endpoint")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Name of the cache engine to be used for this cache cluster.
        Valid values for this parameter are `memcached` or `redis`
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        Version number of the cache engine to be used.
        See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
        in the AWS Documentation center for supported versions
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[str]:
        """
        Specifies the weekly time range for when maintenance
        on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
        The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[str]:
        """
        The compute and memory capacity of the nodes. See
        [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
        supported node types
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> pulumi.Output[Optional[str]]:
        """
        An Amazon Resource Name (ARN) of an
        SNS topic to send ElastiCache notifications to. Example:
        `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
        """
        return pulumi.get(self, "notification_topic_arn")

    @property
    @pulumi.getter(name="numCacheNodes")
    def num_cache_nodes(self) -> pulumi.Output[int]:
        """
        The initial number of cache nodes that the
        cache cluster will have. For Redis, this value must be 1. For Memcache, this
        value must be between 1 and 20. If this number is reduced on subsequent runs,
        the highest numbered nodes will be removed.
        """
        return pulumi.get(self, "num_cache_nodes")

    @property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[str]:
        """
        Name of the parameter group to associate
        with this cache cluster
        """
        return pulumi.get(self, "parameter_group_name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredAvailabilityZones")
    def preferred_availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
        """
        return pulumi.get(self, "preferred_availability_zones")

    @property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
        """
        return pulumi.get(self, "replication_group_id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        One or more VPC security groups associated
        with the cache cluster
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> pulumi.Output[Sequence[str]]:
        """
        List of security group
        names to associate with this cache cluster
        """
        return pulumi.get(self, "security_group_names")

    @property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A single-element string list containing an
        Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
        Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        """
        return pulumi.get(self, "snapshot_arns")

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
        """
        return pulumi.get(self, "snapshot_name")

    @property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> pulumi.Output[Optional[int]]:
        """
        The number of days for which ElastiCache will
        retain automatic cache cluster snapshots before deleting them. For example, if you set
        SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
        before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
        """
        return pulumi.get(self, "snapshot_retention_limit")

    @property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> pulumi.Output[str]:
        """
        The daily time range (in UTC) during which ElastiCache will
        begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
        """
        return pulumi.get(self, "snapshot_window")

    @property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> pulumi.Output[str]:
        """
        Name of the subnet group to be used
        for the cache cluster.
        """
        return pulumi.get(self, "subnet_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

