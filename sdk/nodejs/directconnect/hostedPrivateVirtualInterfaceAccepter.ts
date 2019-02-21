// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides a resource to manage the accepter's side of a Direct Connect hosted private virtual interface.
 * This resource accepts ownership of a private virtual interface created by another AWS account.
 */
export class HostedPrivateVirtualInterfaceAccepter extends pulumi.CustomResource {
    /**
     * Get an existing HostedPrivateVirtualInterfaceAccepter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostedPrivateVirtualInterfaceAccepterState, opts?: pulumi.CustomResourceOptions): HostedPrivateVirtualInterfaceAccepter {
        return new HostedPrivateVirtualInterfaceAccepter(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<HostedPrivateVirtualInterfaceAccepterResult> {
        return ctx.list({...args, type: 'aws:directconnect/hostedPrivateVirtualInterfaceAccepter:HostedPrivateVirtualInterfaceAccepter'});
    }

    /**
     * The ARN of the virtual interface.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The ID of the Direct Connect gateway to which to connect the virtual interface.
     */
    public readonly dxGatewayId: pulumi.Output<string | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The ID of the Direct Connect virtual interface to accept.
     */
    public readonly virtualInterfaceId: pulumi.Output<string>;
    /**
     * The ID of the virtual private gateway to which to connect the virtual interface.
     */
    public readonly vpnGatewayId: pulumi.Output<string | undefined>;

    /**
     * Create a HostedPrivateVirtualInterfaceAccepter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: HostedPrivateVirtualInterfaceAccepterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: HostedPrivateVirtualInterfaceAccepterArgs | HostedPrivateVirtualInterfaceAccepterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: HostedPrivateVirtualInterfaceAccepterState = argsOrState as HostedPrivateVirtualInterfaceAccepterState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["dxGatewayId"] = state ? state.dxGatewayId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["virtualInterfaceId"] = state ? state.virtualInterfaceId : undefined;
            inputs["vpnGatewayId"] = state ? state.vpnGatewayId : undefined;
        } else {
            const args = argsOrState as HostedPrivateVirtualInterfaceAccepterArgs | undefined;
            if (!args || args.virtualInterfaceId === undefined) {
                throw new Error("Missing required property 'virtualInterfaceId'");
            }
            inputs["dxGatewayId"] = args ? args.dxGatewayId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["virtualInterfaceId"] = args ? args.virtualInterfaceId : undefined;
            inputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:directconnect/hostedPrivateVirtualInterfaceAccepter:HostedPrivateVirtualInterfaceAccepter", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering HostedPrivateVirtualInterfaceAccepter resources.
 */
export interface HostedPrivateVirtualInterfaceAccepterState {
    /**
     * The ARN of the virtual interface.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway to which to connect the virtual interface.
     */
    readonly dxGatewayId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The ID of the Direct Connect virtual interface to accept.
     */
    readonly virtualInterfaceId?: pulumi.Input<string>;
    /**
     * The ID of the virtual private gateway to which to connect the virtual interface.
     */
    readonly vpnGatewayId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a HostedPrivateVirtualInterfaceAccepter resource.
 */
export interface HostedPrivateVirtualInterfaceAccepterArgs {
    /**
     * The ID of the Direct Connect gateway to which to connect the virtual interface.
     */
    readonly dxGatewayId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The ID of the Direct Connect virtual interface to accept.
     */
    readonly virtualInterfaceId: pulumi.Input<string>;
    /**
     * The ID of the virtual private gateway to which to connect the virtual interface.
     */
    readonly vpnGatewayId?: pulumi.Input<string>;
}

/**
 * The live HostedPrivateVirtualInterfaceAccepter resource.
 */
export interface HostedPrivateVirtualInterfaceAccepterResult {
    /**
     * The ARN of the virtual interface.
     */
    readonly arn: string;
    /**
     * The ID of the Direct Connect gateway to which to connect the virtual interface.
     */
    readonly dxGatewayId?: string;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: {[key: string]: any};
    /**
     * The ID of the Direct Connect virtual interface to accept.
     */
    readonly virtualInterfaceId: string;
    /**
     * The ID of the virtual private gateway to which to connect the virtual interface.
     */
    readonly vpnGatewayId?: string;
}
