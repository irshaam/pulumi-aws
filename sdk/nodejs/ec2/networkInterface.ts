// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an Elastic network interface (ENI) resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const test = new aws.ec2.NetworkInterface("test", {
 *     attachments: [{
 *         deviceIndex: 1,
 *         instance: aws_instance_test.id,
 *     }],
 *     privateIps: ["10.0.0.50"],
 *     securityGroups: [aws_security_group_web.id],
 *     subnetId: aws_subnet_public_a.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface.html.markdown.
 */
export class NetworkInterface extends pulumi.CustomResource {
    /**
     * Get an existing NetworkInterface resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceState, opts?: pulumi.CustomResourceOptions): NetworkInterface {
        return new NetworkInterface(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/networkInterface:NetworkInterface';

    /**
     * Returns true if the given object is an instance of NetworkInterface.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkInterface {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkInterface.__pulumiType;
    }

    /**
     * Block to define the attachment of the ENI. Documented below.
     */
    public readonly attachments!: pulumi.Output<{ attachmentId: string, deviceIndex: number, instance: string }[]>;
    /**
     * A description for the network interface.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly privateDnsName!: pulumi.Output<string>;
    public readonly privateIp!: pulumi.Output<string>;
    /**
     * List of private IPs to assign to the ENI.
     */
    public readonly privateIps!: pulumi.Output<string[]>;
    /**
     * Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default. 
     */
    public readonly privateIpsCount!: pulumi.Output<number>;
    /**
     * List of security group IDs to assign to the ENI.
     */
    public readonly securityGroups!: pulumi.Output<string[]>;
    /**
     * Whether to enable source destination checking for the ENI. Default true.
     */
    public readonly sourceDestCheck!: pulumi.Output<boolean | undefined>;
    /**
     * Subnet ID to create the ENI in.
     */
    public readonly subnetId!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a NetworkInterface resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkInterfaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkInterfaceArgs | NetworkInterfaceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NetworkInterfaceState | undefined;
            inputs["attachments"] = state ? state.attachments : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["privateDnsName"] = state ? state.privateDnsName : undefined;
            inputs["privateIp"] = state ? state.privateIp : undefined;
            inputs["privateIps"] = state ? state.privateIps : undefined;
            inputs["privateIpsCount"] = state ? state.privateIpsCount : undefined;
            inputs["securityGroups"] = state ? state.securityGroups : undefined;
            inputs["sourceDestCheck"] = state ? state.sourceDestCheck : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as NetworkInterfaceArgs | undefined;
            if (!args || args.subnetId === undefined) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["attachments"] = args ? args.attachments : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["privateIp"] = args ? args.privateIp : undefined;
            inputs["privateIps"] = args ? args.privateIps : undefined;
            inputs["privateIpsCount"] = args ? args.privateIpsCount : undefined;
            inputs["securityGroups"] = args ? args.securityGroups : undefined;
            inputs["sourceDestCheck"] = args ? args.sourceDestCheck : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["privateDnsName"] = undefined /*out*/;
        }
        super(NetworkInterface.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkInterface resources.
 */
export interface NetworkInterfaceState {
    /**
     * Block to define the attachment of the ENI. Documented below.
     */
    readonly attachments?: pulumi.Input<pulumi.Input<{ attachmentId?: pulumi.Input<string>, deviceIndex: pulumi.Input<number>, instance: pulumi.Input<string> }>[]>;
    /**
     * A description for the network interface.
     */
    readonly description?: pulumi.Input<string>;
    readonly privateDnsName?: pulumi.Input<string>;
    readonly privateIp?: pulumi.Input<string>;
    /**
     * List of private IPs to assign to the ENI.
     */
    readonly privateIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default. 
     */
    readonly privateIpsCount?: pulumi.Input<number>;
    /**
     * List of security group IDs to assign to the ENI.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether to enable source destination checking for the ENI. Default true.
     */
    readonly sourceDestCheck?: pulumi.Input<boolean>;
    /**
     * Subnet ID to create the ENI in.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a NetworkInterface resource.
 */
export interface NetworkInterfaceArgs {
    /**
     * Block to define the attachment of the ENI. Documented below.
     */
    readonly attachments?: pulumi.Input<pulumi.Input<{ attachmentId?: pulumi.Input<string>, deviceIndex: pulumi.Input<number>, instance: pulumi.Input<string> }>[]>;
    /**
     * A description for the network interface.
     */
    readonly description?: pulumi.Input<string>;
    readonly privateIp?: pulumi.Input<string>;
    /**
     * List of private IPs to assign to the ENI.
     */
    readonly privateIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default. 
     */
    readonly privateIpsCount?: pulumi.Input<number>;
    /**
     * List of security group IDs to assign to the ENI.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether to enable source destination checking for the ENI. Default true.
     */
    readonly sourceDestCheck?: pulumi.Input<boolean>;
    /**
     * Subnet ID to create the ENI in.
     */
    readonly subnetId: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
