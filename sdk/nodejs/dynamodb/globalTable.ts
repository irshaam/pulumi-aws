// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.
 * 
 * > Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the [AWS DynamoDB Global Table Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html) for more information.
 */
export class GlobalTable extends pulumi.CustomResource {
    /**
     * Get an existing GlobalTable resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalTableState, opts?: pulumi.CustomResourceOptions): GlobalTable {
        return new GlobalTable(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:dynamodb/globalTable:GlobalTable';

    /**
     * Returns true if the given object is an instance of GlobalTable.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GlobalTable {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GlobalTable.__pulumiType;
    }

    /**
     * The ARN of the DynamoDB Global Table
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name of the global table. Must match underlying DynamoDB Table names in all regions.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Underlying DynamoDB Table. At least 1 replica must be defined. See below.
     */
    public readonly replicas!: pulumi.Output<{ regionName: string }[]>;

    /**
     * Create a GlobalTable resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GlobalTableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GlobalTableArgs | GlobalTableState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GlobalTableState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["replicas"] = state ? state.replicas : undefined;
        } else {
            const args = argsOrState as GlobalTableArgs | undefined;
            if (!args || args.replicas === undefined) {
                throw new Error("Missing required property 'replicas'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["replicas"] = args ? args.replicas : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super(GlobalTable.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GlobalTable resources.
 */
export interface GlobalTableState {
    /**
     * The ARN of the DynamoDB Global Table
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of the global table. Must match underlying DynamoDB Table names in all regions.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Underlying DynamoDB Table. At least 1 replica must be defined. See below.
     */
    readonly replicas?: pulumi.Input<pulumi.Input<{ regionName: pulumi.Input<string> }>[]>;
}

/**
 * The set of arguments for constructing a GlobalTable resource.
 */
export interface GlobalTableArgs {
    /**
     * The name of the global table. Must match underlying DynamoDB Table names in all regions.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Underlying DynamoDB Table. At least 1 replica must be defined. See below.
     */
    readonly replicas: pulumi.Input<pulumi.Input<{ regionName: pulumi.Input<string> }>[]>;
}
