// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class DefaultSecurityGroup extends pulumi.CustomResource {
    /**
     * Get an existing DefaultSecurityGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultSecurityGroupState, opts?: pulumi.CustomResourceOptions): DefaultSecurityGroup {
        return new DefaultSecurityGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/defaultSecurityGroup:DefaultSecurityGroup';

    /**
     * Returns true if the given object is an instance of DefaultSecurityGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DefaultSecurityGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DefaultSecurityGroup.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    public readonly egress!: pulumi.Output<{ cidrBlocks?: string[], description?: string, fromPort: number, ipv6CidrBlocks?: string[], prefixListIds?: string[], protocol: string, securityGroups?: string[], self?: boolean, toPort: number }[] | undefined>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    public readonly ingress!: pulumi.Output<{ cidrBlocks?: string[], description?: string, fromPort: number, ipv6CidrBlocks?: string[], prefixListIds?: string[], protocol: string, securityGroups?: string[], self?: boolean, toPort: number }[] | undefined>;
    /**
     * The name of the security group
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The owner ID.
     */
    public /*out*/ readonly ownerId!: pulumi.Output<string>;
    public readonly revokeRulesOnDelete!: pulumi.Output<boolean | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The VPC ID. **Note that changing
     * the `vpc_id` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a DefaultSecurityGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DefaultSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DefaultSecurityGroupArgs | DefaultSecurityGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DefaultSecurityGroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["egress"] = state ? state.egress : undefined;
            inputs["ingress"] = state ? state.ingress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["revokeRulesOnDelete"] = state ? state.revokeRulesOnDelete : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as DefaultSecurityGroupArgs | undefined;
            inputs["egress"] = args ? args.egress : undefined;
            inputs["ingress"] = args ? args.ingress : undefined;
            inputs["revokeRulesOnDelete"] = args ? args.revokeRulesOnDelete : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
        }
        super(DefaultSecurityGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DefaultSecurityGroup resources.
 */
export interface DefaultSecurityGroupState {
    readonly arn?: pulumi.Input<string>;
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    readonly egress?: pulumi.Input<pulumi.Input<{ cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, description?: pulumi.Input<string>, fromPort: pulumi.Input<number>, ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, prefixListIds?: pulumi.Input<pulumi.Input<string>[]>, protocol: pulumi.Input<string>, securityGroups?: pulumi.Input<pulumi.Input<string>[]>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    readonly ingress?: pulumi.Input<pulumi.Input<{ cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, description?: pulumi.Input<string>, fromPort: pulumi.Input<number>, ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, prefixListIds?: pulumi.Input<pulumi.Input<string>[]>, protocol: pulumi.Input<string>, securityGroups?: pulumi.Input<pulumi.Input<string>[]>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
    /**
     * The name of the security group
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The owner ID.
     */
    readonly ownerId?: pulumi.Input<string>;
    readonly revokeRulesOnDelete?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The VPC ID. **Note that changing
     * the `vpc_id` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DefaultSecurityGroup resource.
 */
export interface DefaultSecurityGroupArgs {
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    readonly egress?: pulumi.Input<pulumi.Input<{ cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, description?: pulumi.Input<string>, fromPort: pulumi.Input<number>, ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, prefixListIds?: pulumi.Input<pulumi.Input<string>[]>, protocol: pulumi.Input<string>, securityGroups?: pulumi.Input<pulumi.Input<string>[]>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    readonly ingress?: pulumi.Input<pulumi.Input<{ cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, description?: pulumi.Input<string>, fromPort: pulumi.Input<number>, ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>, prefixListIds?: pulumi.Input<pulumi.Input<string>[]>, protocol: pulumi.Input<string>, securityGroups?: pulumi.Input<pulumi.Input<string>[]>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
    readonly revokeRulesOnDelete?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The VPC ID. **Note that changing
     * the `vpc_id` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    readonly vpcId?: pulumi.Input<string>;
}
