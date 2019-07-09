// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class DefaultRouteTable extends pulumi.CustomResource {
    /**
     * Get an existing DefaultRouteTable resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultRouteTableState, opts?: pulumi.CustomResourceOptions): DefaultRouteTable {
        return new DefaultRouteTable(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/defaultRouteTable:DefaultRouteTable';

    /**
     * Returns true if the given object is an instance of DefaultRouteTable.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DefaultRouteTable {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DefaultRouteTable.__pulumiType;
    }

    /**
     * The ID of the Default Routing Table.
     */
    public readonly defaultRouteTableId!: pulumi.Output<string>;
    /**
     * The ID of the AWS account that owns the route table
     */
    public /*out*/ readonly ownerId!: pulumi.Output<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    public readonly propagatingVgws!: pulumi.Output<string[] | undefined>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    public readonly routes!: pulumi.Output<{ cidrBlock?: string, egressOnlyGatewayId?: string, gatewayId?: string, instanceId?: string, ipv6CidrBlock?: string, natGatewayId?: string, networkInterfaceId?: string, transitGatewayId?: string, vpcPeeringConnectionId?: string }[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    public /*out*/ readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a DefaultRouteTable resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DefaultRouteTableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DefaultRouteTableArgs | DefaultRouteTableState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DefaultRouteTableState | undefined;
            inputs["defaultRouteTableId"] = state ? state.defaultRouteTableId : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["propagatingVgws"] = state ? state.propagatingVgws : undefined;
            inputs["routes"] = state ? state.routes : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as DefaultRouteTableArgs | undefined;
            if (!args || args.defaultRouteTableId === undefined) {
                throw new Error("Missing required property 'defaultRouteTableId'");
            }
            inputs["defaultRouteTableId"] = args ? args.defaultRouteTableId : undefined;
            inputs["propagatingVgws"] = args ? args.propagatingVgws : undefined;
            inputs["routes"] = args ? args.routes : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["ownerId"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
        }
        super(DefaultRouteTable.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DefaultRouteTable resources.
 */
export interface DefaultRouteTableState {
    /**
     * The ID of the Default Routing Table.
     */
    readonly defaultRouteTableId?: pulumi.Input<string>;
    /**
     * The ID of the AWS account that owns the route table
     */
    readonly ownerId?: pulumi.Input<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    readonly propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    readonly routes?: pulumi.Input<pulumi.Input<{ cidrBlock?: pulumi.Input<string>, egressOnlyGatewayId?: pulumi.Input<string>, gatewayId?: pulumi.Input<string>, instanceId?: pulumi.Input<string>, ipv6CidrBlock?: pulumi.Input<string>, natGatewayId?: pulumi.Input<string>, networkInterfaceId?: pulumi.Input<string>, transitGatewayId?: pulumi.Input<string>, vpcPeeringConnectionId?: pulumi.Input<string> }>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DefaultRouteTable resource.
 */
export interface DefaultRouteTableArgs {
    /**
     * The ID of the Default Routing Table.
     */
    readonly defaultRouteTableId: pulumi.Input<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    readonly propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    readonly routes?: pulumi.Input<pulumi.Input<{ cidrBlock?: pulumi.Input<string>, egressOnlyGatewayId?: pulumi.Input<string>, gatewayId?: pulumi.Input<string>, instanceId?: pulumi.Input<string>, ipv6CidrBlock?: pulumi.Input<string>, natGatewayId?: pulumi.Input<string>, networkInterfaceId?: pulumi.Input<string>, transitGatewayId?: pulumi.Input<string>, vpcPeeringConnectionId?: pulumi.Input<string> }>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
