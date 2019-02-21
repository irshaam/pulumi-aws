// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Manages an EC2 Transit Gateway Route Table association.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.ec2transitgateway.RouteTableAssociation("example", {
 *     transitGatewayAttachmentId: aws_ec2_transit_gateway_vpc_attachment_example.id,
 *     transitGatewayRouteTableId: aws_ec2_transit_gateway_route_table_example.id,
 * });
 * ```
 */
export class RouteTableAssociation extends pulumi.CustomResource {
    /**
     * Get an existing RouteTableAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableAssociationState, opts?: pulumi.CustomResourceOptions): RouteTableAssociation {
        return new RouteTableAssociation(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<RouteTableAssociationResult> {
        return ctx.list({...args, type: 'aws:ec2transitgateway/routeTableAssociation:RouteTableAssociation'});
    }

    /**
     * Identifier of the resource
     */
    public /*out*/ readonly resourceId: pulumi.Output<string>;
    /**
     * Type of the resource
     */
    public /*out*/ readonly resourceType: pulumi.Output<string>;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    public readonly transitGatewayAttachmentId: pulumi.Output<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    public readonly transitGatewayRouteTableId: pulumi.Output<string>;

    /**
     * Create a RouteTableAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RouteTableAssociationArgs | RouteTableAssociationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: RouteTableAssociationState = argsOrState as RouteTableAssociationState | undefined;
            inputs["resourceId"] = state ? state.resourceId : undefined;
            inputs["resourceType"] = state ? state.resourceType : undefined;
            inputs["transitGatewayAttachmentId"] = state ? state.transitGatewayAttachmentId : undefined;
            inputs["transitGatewayRouteTableId"] = state ? state.transitGatewayRouteTableId : undefined;
        } else {
            const args = argsOrState as RouteTableAssociationArgs | undefined;
            if (!args || args.transitGatewayAttachmentId === undefined) {
                throw new Error("Missing required property 'transitGatewayAttachmentId'");
            }
            if (!args || args.transitGatewayRouteTableId === undefined) {
                throw new Error("Missing required property 'transitGatewayRouteTableId'");
            }
            inputs["transitGatewayAttachmentId"] = args ? args.transitGatewayAttachmentId : undefined;
            inputs["transitGatewayRouteTableId"] = args ? args.transitGatewayRouteTableId : undefined;
            inputs["resourceId"] = undefined /*out*/;
            inputs["resourceType"] = undefined /*out*/;
        }
        super("aws:ec2transitgateway/routeTableAssociation:RouteTableAssociation", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RouteTableAssociation resources.
 */
export interface RouteTableAssociationState {
    /**
     * Identifier of the resource
     */
    readonly resourceId?: pulumi.Input<string>;
    /**
     * Type of the resource
     */
    readonly resourceType?: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    readonly transitGatewayAttachmentId?: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    readonly transitGatewayRouteTableId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RouteTableAssociation resource.
 */
export interface RouteTableAssociationArgs {
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    readonly transitGatewayAttachmentId: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    readonly transitGatewayRouteTableId: pulumi.Input<string>;
}

/**
 * The live RouteTableAssociation resource.
 */
export interface RouteTableAssociationResult {
    /**
     * Identifier of the resource
     */
    readonly resourceId: string;
    /**
     * Type of the resource
     */
    readonly resourceType: string;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    readonly transitGatewayAttachmentId: string;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    readonly transitGatewayRouteTableId: string;
}
