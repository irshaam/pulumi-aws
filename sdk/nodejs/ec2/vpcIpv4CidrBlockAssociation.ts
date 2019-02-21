// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides a resource to associate additional IPv4 CIDR blocks with a VPC.
 * 
 * When a VPC is created, a primary IPv4 CIDR block for the VPC must be specified.
 * The `aws_vpc_ipv4_cidr_block_association` resource allows further IPv4 CIDR blocks to be added to the VPC.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const main = new aws.ec2.Vpc("main", {
 *     cidrBlock: "10.0.0.0/16",
 * });
 * const secondaryCidr = new aws.ec2.VpcIpv4CidrBlockAssociation("secondary_cidr", {
 *     cidrBlock: "172.2.0.0/16",
 *     vpcId: main.id,
 * });
 * ```
 */
export class VpcIpv4CidrBlockAssociation extends pulumi.CustomResource {
    /**
     * Get an existing VpcIpv4CidrBlockAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcIpv4CidrBlockAssociationState, opts?: pulumi.CustomResourceOptions): VpcIpv4CidrBlockAssociation {
        return new VpcIpv4CidrBlockAssociation(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<VpcIpv4CidrBlockAssociationResult> {
        return ctx.list({...args, type: 'aws:ec2/vpcIpv4CidrBlockAssociation:VpcIpv4CidrBlockAssociation'});
    }

    /**
     * The additional IPv4 CIDR block to associate with the VPC.
     */
    public readonly cidrBlock: pulumi.Output<string>;
    /**
     * The ID of the VPC to make the association with.
     */
    public readonly vpcId: pulumi.Output<string>;

    /**
     * Create a VpcIpv4CidrBlockAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcIpv4CidrBlockAssociationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VpcIpv4CidrBlockAssociationArgs | VpcIpv4CidrBlockAssociationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VpcIpv4CidrBlockAssociationState = argsOrState as VpcIpv4CidrBlockAssociationState | undefined;
            inputs["cidrBlock"] = state ? state.cidrBlock : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as VpcIpv4CidrBlockAssociationArgs | undefined;
            if (!args || args.cidrBlock === undefined) {
                throw new Error("Missing required property 'cidrBlock'");
            }
            if (!args || args.vpcId === undefined) {
                throw new Error("Missing required property 'vpcId'");
            }
            inputs["cidrBlock"] = args ? args.cidrBlock : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
        }
        super("aws:ec2/vpcIpv4CidrBlockAssociation:VpcIpv4CidrBlockAssociation", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VpcIpv4CidrBlockAssociation resources.
 */
export interface VpcIpv4CidrBlockAssociationState {
    /**
     * The additional IPv4 CIDR block to associate with the VPC.
     */
    readonly cidrBlock?: pulumi.Input<string>;
    /**
     * The ID of the VPC to make the association with.
     */
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VpcIpv4CidrBlockAssociation resource.
 */
export interface VpcIpv4CidrBlockAssociationArgs {
    /**
     * The additional IPv4 CIDR block to associate with the VPC.
     */
    readonly cidrBlock: pulumi.Input<string>;
    /**
     * The ID of the VPC to make the association with.
     */
    readonly vpcId: pulumi.Input<string>;
}

/**
 * The live VpcIpv4CidrBlockAssociation resource.
 */
export interface VpcIpv4CidrBlockAssociationResult {
    /**
     * The additional IPv4 CIDR block to associate with the VPC.
     */
    readonly cidrBlock: string;
    /**
     * The ID of the VPC to make the association with.
     */
    readonly vpcId: string;
}
