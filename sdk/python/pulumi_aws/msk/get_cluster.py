# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, arn=None, bootstrap_brokers=None, cluster_name=None, kafka_version=None, number_of_broker_nodes=None, tags=None, zookeeper_connect_string=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        Amazon Resource Name (ARN) of the MSK cluster.
        """
        if bootstrap_brokers and not isinstance(bootstrap_brokers, str):
            raise TypeError("Expected argument 'bootstrap_brokers' to be a str")
        __self__.bootstrap_brokers = bootstrap_brokers
        """
        A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.
        """
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        __self__.cluster_name = cluster_name
        if kafka_version and not isinstance(kafka_version, str):
            raise TypeError("Expected argument 'kafka_version' to be a str")
        __self__.kafka_version = kafka_version
        """
        Apache Kafka version.
        """
        if number_of_broker_nodes and not isinstance(number_of_broker_nodes, float):
            raise TypeError("Expected argument 'number_of_broker_nodes' to be a float")
        __self__.number_of_broker_nodes = number_of_broker_nodes
        """
        Number of broker nodes in the cluster.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Map of key-value pairs assigned to the cluster.
        """
        if zookeeper_connect_string and not isinstance(zookeeper_connect_string, str):
            raise TypeError("Expected argument 'zookeeper_connect_string' to be a str")
        __self__.zookeeper_connect_string = zookeeper_connect_string
        """
        A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_cluster(cluster_name=None,tags=None,opts=None):
    """
    Get information on an Amazon MSK Cluster.
    """
    __args__ = dict()

    __args__['clusterName'] = cluster_name
    __args__['tags'] = tags
    __ret__ = await pulumi.runtime.invoke('aws:msk/getCluster:getCluster', __args__, opts=opts)

    return GetClusterResult(
        arn=__ret__.get('arn'),
        bootstrap_brokers=__ret__.get('bootstrapBrokers'),
        cluster_name=__ret__.get('clusterName'),
        kafka_version=__ret__.get('kafkaVersion'),
        number_of_broker_nodes=__ret__.get('numberOfBrokerNodes'),
        tags=__ret__.get('tags'),
        zookeeper_connect_string=__ret__.get('zookeeperConnectString'),
        id=__ret__.get('id'))
