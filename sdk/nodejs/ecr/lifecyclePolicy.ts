// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Manages an ECR repository lifecycle policy.
 * 
 * > **NOTE:** Only one `aws_ecr_lifecycle_policy` resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the `policy` JSON.
 * 
 * > **NOTE:** The AWS ECR API seems to reorder rules based on `rulePriority`. If you define multiple rules that are not sorted in ascending `rulePriority` order in the Terraform code, the resource will be flagged for recreation every `terraform plan`.
 * 
 * ## Example Usage
 * 
 * ### Policy on untagged image
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const foo = new aws.ecr.Repository("foo", {});
 * const foopolicy = new aws.ecr.LifecyclePolicy("foopolicy", {
 *     policy: `{
 *     "rules": [
 *         {
 *             "rulePriority": 1,
 *             "description": "Expire images older than 14 days",
 *             "selection": {
 *                 "tagStatus": "untagged",
 *                 "countType": "sinceImagePushed",
 *                 "countUnit": "days",
 *                 "countNumber": 14
 *             },
 *             "action": {
 *                 "type": "expire"
 *             }
 *         }
 *     ]
 * }
 * `,
 *     repository: foo.name,
 * });
 * ```
 * 
 * ### Policy on tagged image
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const foo = new aws.ecr.Repository("foo", {});
 * const foopolicy = new aws.ecr.LifecyclePolicy("foopolicy", {
 *     policy: `{
 *     "rules": [
 *         {
 *             "rulePriority": 1,
 *             "description": "Keep last 30 images",
 *             "selection": {
 *                 "tagStatus": "tagged",
 *                 "tagPrefixList": ["v"],
 *                 "countType": "imageCountMoreThan",
 *                 "countNumber": 30
 *             },
 *             "action": {
 *                 "type": "expire"
 *             }
 *         }
 *     ]
 * }
 * `,
 *     repository: foo.name,
 * });
 * ```
 */
export class LifecyclePolicy extends pulumi.CustomResource {
    /**
     * Get an existing LifecyclePolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LifecyclePolicyState, opts?: pulumi.CustomResourceOptions): LifecyclePolicy {
        return new LifecyclePolicy(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<LifecyclePolicyResult> {
        return ctx.list({...args, type: 'aws:ecr/lifecyclePolicy:LifecyclePolicy'});
    }

    /**
     * The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    public readonly policy: pulumi.Output<string>;
    /**
     * The registry ID where the repository was created.
     */
    public /*out*/ readonly registryId: pulumi.Output<string>;
    /**
     * Name of the repository to apply the policy.
     */
    public readonly repository: pulumi.Output<string>;

    /**
     * Create a LifecyclePolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LifecyclePolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LifecyclePolicyArgs | LifecyclePolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: LifecyclePolicyState = argsOrState as LifecyclePolicyState | undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["registryId"] = state ? state.registryId : undefined;
            inputs["repository"] = state ? state.repository : undefined;
        } else {
            const args = argsOrState as LifecyclePolicyArgs | undefined;
            if (!args || args.policy === undefined) {
                throw new Error("Missing required property 'policy'");
            }
            if (!args || args.repository === undefined) {
                throw new Error("Missing required property 'repository'");
            }
            inputs["policy"] = args ? args.policy : undefined;
            inputs["repository"] = args ? args.repository : undefined;
            inputs["registryId"] = undefined /*out*/;
        }
        super("aws:ecr/lifecyclePolicy:LifecyclePolicy", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LifecyclePolicy resources.
 */
export interface LifecyclePolicyState {
    /**
     * The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * The registry ID where the repository was created.
     */
    readonly registryId?: pulumi.Input<string>;
    /**
     * Name of the repository to apply the policy.
     */
    readonly repository?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LifecyclePolicy resource.
 */
export interface LifecyclePolicyArgs {
    /**
     * The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    readonly policy: pulumi.Input<string>;
    /**
     * Name of the repository to apply the policy.
     */
    readonly repository: pulumi.Input<string>;
}

/**
 * The live LifecyclePolicy resource.
 */
export interface LifecyclePolicyResult {
    /**
     * The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    readonly policy: string;
    /**
     * The registry ID where the repository was created.
     */
    readonly registryId: string;
    /**
     * Name of the repository to apply the policy.
     */
    readonly repository: string;
}
