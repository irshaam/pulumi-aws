// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a DAX Cluster resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const bar = new aws.dax.Cluster("bar", {
 *     clusterName: "cluster-example",
 *     iamRoleArn: aws_iam_role_example.arn,
 *     nodeType: "dax.r4.large",
 *     replicationFactor: 1,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown.
 */
export class Cluster extends pulumi.CustomResource {
    /**
     * Get an existing Cluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:dax/cluster:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }

    /**
     * The ARN of the DAX cluster
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * List of Availability Zones in which the
     * nodes will be created
     */
    public readonly availabilityZones!: pulumi.Output<string[] | undefined>;
    /**
     * The DNS name of the DAX cluster without the port appended
     */
    public /*out*/ readonly clusterAddress!: pulumi.Output<string>;
    /**
     * Group identifier. DAX converts this name to
     * lowercase
     */
    public readonly clusterName!: pulumi.Output<string>;
    /**
     * The configuration endpoint for this DAX cluster,
     * consisting of a DNS name and a port number
     */
    public /*out*/ readonly configurationEndpoint!: pulumi.Output<string>;
    /**
     * Description for the cluster
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A valid Amazon Resource Name (ARN) that identifies
     * an IAM role. At runtime, DAX will assume this role and use the role's
     * permissions to access DynamoDB on your behalf
     */
    public readonly iamRoleArn!: pulumi.Output<string>;
    /**
     * Specifies the weekly time range for when
     * maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
     * (24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
     * `sun:05:00-sun:09:00`
     */
    public readonly maintenanceWindow!: pulumi.Output<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Nodes][1] for supported node types
     */
    public readonly nodeType!: pulumi.Output<string>;
    /**
     * List of node objects including `id`, `address`, `port` and
     * `availability_zone`. Referenceable e.g. as
     * `${aws_dax_cluster.test.nodes.0.address}`
     */
    public /*out*/ readonly nodes!: pulumi.Output<{ address: string, availabilityZone: string, id: string, port: number }[]>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send DAX notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    public readonly notificationTopicArn!: pulumi.Output<string | undefined>;
    /**
     * Name of the parameter group to associate
     * with this DAX cluster
     */
    public readonly parameterGroupName!: pulumi.Output<string>;
    /**
     * The port used by the configuration endpoint
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    /**
     * The number of nodes in the DAX cluster. A
     * replication factor of 1 will create a single-node cluster, without any read
     * replicas
     */
    public readonly replicationFactor!: pulumi.Output<number>;
    /**
     * One or more VPC security groups associated
     * with the cluster
     */
    public readonly securityGroupIds!: pulumi.Output<string[]>;
    /**
     * Encrypt at rest options
     */
    public readonly serverSideEncryption!: pulumi.Output<{ enabled?: boolean } | undefined>;
    /**
     * Name of the subnet group to be used for the
     * cluster
     */
    public readonly subnetGroupName!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterArgs | ClusterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ClusterState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["availabilityZones"] = state ? state.availabilityZones : undefined;
            inputs["clusterAddress"] = state ? state.clusterAddress : undefined;
            inputs["clusterName"] = state ? state.clusterName : undefined;
            inputs["configurationEndpoint"] = state ? state.configurationEndpoint : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["iamRoleArn"] = state ? state.iamRoleArn : undefined;
            inputs["maintenanceWindow"] = state ? state.maintenanceWindow : undefined;
            inputs["nodeType"] = state ? state.nodeType : undefined;
            inputs["nodes"] = state ? state.nodes : undefined;
            inputs["notificationTopicArn"] = state ? state.notificationTopicArn : undefined;
            inputs["parameterGroupName"] = state ? state.parameterGroupName : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["replicationFactor"] = state ? state.replicationFactor : undefined;
            inputs["securityGroupIds"] = state ? state.securityGroupIds : undefined;
            inputs["serverSideEncryption"] = state ? state.serverSideEncryption : undefined;
            inputs["subnetGroupName"] = state ? state.subnetGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ClusterArgs | undefined;
            if (!args || args.clusterName === undefined) {
                throw new Error("Missing required property 'clusterName'");
            }
            if (!args || args.iamRoleArn === undefined) {
                throw new Error("Missing required property 'iamRoleArn'");
            }
            if (!args || args.nodeType === undefined) {
                throw new Error("Missing required property 'nodeType'");
            }
            if (!args || args.replicationFactor === undefined) {
                throw new Error("Missing required property 'replicationFactor'");
            }
            inputs["availabilityZones"] = args ? args.availabilityZones : undefined;
            inputs["clusterName"] = args ? args.clusterName : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["iamRoleArn"] = args ? args.iamRoleArn : undefined;
            inputs["maintenanceWindow"] = args ? args.maintenanceWindow : undefined;
            inputs["nodeType"] = args ? args.nodeType : undefined;
            inputs["notificationTopicArn"] = args ? args.notificationTopicArn : undefined;
            inputs["parameterGroupName"] = args ? args.parameterGroupName : undefined;
            inputs["replicationFactor"] = args ? args.replicationFactor : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["serverSideEncryption"] = args ? args.serverSideEncryption : undefined;
            inputs["subnetGroupName"] = args ? args.subnetGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["clusterAddress"] = undefined /*out*/;
            inputs["configurationEndpoint"] = undefined /*out*/;
            inputs["nodes"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
        }
        super(Cluster.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Cluster resources.
 */
export interface ClusterState {
    /**
     * The ARN of the DAX cluster
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * List of Availability Zones in which the
     * nodes will be created
     */
    readonly availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The DNS name of the DAX cluster without the port appended
     */
    readonly clusterAddress?: pulumi.Input<string>;
    /**
     * Group identifier. DAX converts this name to
     * lowercase
     */
    readonly clusterName?: pulumi.Input<string>;
    /**
     * The configuration endpoint for this DAX cluster,
     * consisting of a DNS name and a port number
     */
    readonly configurationEndpoint?: pulumi.Input<string>;
    /**
     * Description for the cluster
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A valid Amazon Resource Name (ARN) that identifies
     * an IAM role. At runtime, DAX will assume this role and use the role's
     * permissions to access DynamoDB on your behalf
     */
    readonly iamRoleArn?: pulumi.Input<string>;
    /**
     * Specifies the weekly time range for when
     * maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
     * (24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
     * `sun:05:00-sun:09:00`
     */
    readonly maintenanceWindow?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Nodes][1] for supported node types
     */
    readonly nodeType?: pulumi.Input<string>;
    /**
     * List of node objects including `id`, `address`, `port` and
     * `availability_zone`. Referenceable e.g. as
     * `${aws_dax_cluster.test.nodes.0.address}`
     */
    readonly nodes?: pulumi.Input<pulumi.Input<{ address?: pulumi.Input<string>, availabilityZone?: pulumi.Input<string>, id?: pulumi.Input<string>, port?: pulumi.Input<number> }>[]>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send DAX notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    readonly notificationTopicArn?: pulumi.Input<string>;
    /**
     * Name of the parameter group to associate
     * with this DAX cluster
     */
    readonly parameterGroupName?: pulumi.Input<string>;
    /**
     * The port used by the configuration endpoint
     */
    readonly port?: pulumi.Input<number>;
    /**
     * The number of nodes in the DAX cluster. A
     * replication factor of 1 will create a single-node cluster, without any read
     * replicas
     */
    readonly replicationFactor?: pulumi.Input<number>;
    /**
     * One or more VPC security groups associated
     * with the cluster
     */
    readonly securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Encrypt at rest options
     */
    readonly serverSideEncryption?: pulumi.Input<{ enabled?: pulumi.Input<boolean> }>;
    /**
     * Name of the subnet group to be used for the
     * cluster
     */
    readonly subnetGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    /**
     * List of Availability Zones in which the
     * nodes will be created
     */
    readonly availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Group identifier. DAX converts this name to
     * lowercase
     */
    readonly clusterName: pulumi.Input<string>;
    /**
     * Description for the cluster
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A valid Amazon Resource Name (ARN) that identifies
     * an IAM role. At runtime, DAX will assume this role and use the role's
     * permissions to access DynamoDB on your behalf
     */
    readonly iamRoleArn: pulumi.Input<string>;
    /**
     * Specifies the weekly time range for when
     * maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
     * (24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
     * `sun:05:00-sun:09:00`
     */
    readonly maintenanceWindow?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Nodes][1] for supported node types
     */
    readonly nodeType: pulumi.Input<string>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send DAX notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    readonly notificationTopicArn?: pulumi.Input<string>;
    /**
     * Name of the parameter group to associate
     * with this DAX cluster
     */
    readonly parameterGroupName?: pulumi.Input<string>;
    /**
     * The number of nodes in the DAX cluster. A
     * replication factor of 1 will create a single-node cluster, without any read
     * replicas
     */
    readonly replicationFactor: pulumi.Input<number>;
    /**
     * One or more VPC security groups associated
     * with the cluster
     */
    readonly securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Encrypt at rest options
     */
    readonly serverSideEncryption?: pulumi.Input<{ enabled?: pulumi.Input<boolean> }>;
    /**
     * Name of the subnet group to be used for the
     * cluster
     */
    readonly subnetGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
