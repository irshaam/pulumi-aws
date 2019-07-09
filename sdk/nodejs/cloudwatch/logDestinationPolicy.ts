// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a CloudWatch Logs destination policy resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const testDestination = new aws.cloudwatch.LogDestination("test_destination", {
 *     roleArn: aws_iam_role_iam_for_cloudwatch.arn,
 *     targetArn: aws_kinesis_stream_kinesis_for_cloudwatch.arn,
 * });
 * const testDestinationPolicyPolicyDocument = testDestination.arn.apply(arn => aws.iam.getPolicyDocument({
 *     statements: [{
 *         actions: ["logs:PutSubscriptionFilter"],
 *         effect: "Allow",
 *         principals: [{
 *             identifiers: ["123456789012"],
 *             type: "AWS",
 *         }],
 *         resources: [arn],
 *     }],
 * }));
 * const testDestinationPolicyLogDestinationPolicy = new aws.cloudwatch.LogDestinationPolicy("test_destination_policy", {
 *     accessPolicy: testDestinationPolicyPolicyDocument.json,
 *     destinationName: testDestination.name,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudwatch_log_destination_policy.html.markdown.
 */
export class LogDestinationPolicy extends pulumi.CustomResource {
    /**
     * Get an existing LogDestinationPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogDestinationPolicyState, opts?: pulumi.CustomResourceOptions): LogDestinationPolicy {
        return new LogDestinationPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cloudwatch/logDestinationPolicy:LogDestinationPolicy';

    /**
     * Returns true if the given object is an instance of LogDestinationPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LogDestinationPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LogDestinationPolicy.__pulumiType;
    }

    /**
     * The policy document. This is a JSON formatted string.
     */
    public readonly accessPolicy!: pulumi.Output<string>;
    /**
     * A name for the subscription filter
     */
    public readonly destinationName!: pulumi.Output<string>;

    /**
     * Create a LogDestinationPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LogDestinationPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LogDestinationPolicyArgs | LogDestinationPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LogDestinationPolicyState | undefined;
            inputs["accessPolicy"] = state ? state.accessPolicy : undefined;
            inputs["destinationName"] = state ? state.destinationName : undefined;
        } else {
            const args = argsOrState as LogDestinationPolicyArgs | undefined;
            if (!args || args.accessPolicy === undefined) {
                throw new Error("Missing required property 'accessPolicy'");
            }
            if (!args || args.destinationName === undefined) {
                throw new Error("Missing required property 'destinationName'");
            }
            inputs["accessPolicy"] = args ? args.accessPolicy : undefined;
            inputs["destinationName"] = args ? args.destinationName : undefined;
        }
        super(LogDestinationPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LogDestinationPolicy resources.
 */
export interface LogDestinationPolicyState {
    /**
     * The policy document. This is a JSON formatted string.
     */
    readonly accessPolicy?: pulumi.Input<string>;
    /**
     * A name for the subscription filter
     */
    readonly destinationName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LogDestinationPolicy resource.
 */
export interface LogDestinationPolicyArgs {
    /**
     * The policy document. This is a JSON formatted string.
     */
    readonly accessPolicy: pulumi.Input<string>;
    /**
     * A name for the subscription filter
     */
    readonly destinationName: pulumi.Input<string>;
}
