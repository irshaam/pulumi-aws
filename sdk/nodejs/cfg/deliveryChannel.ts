// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides an AWS Config Delivery Channel.
 * 
 * > **Note:** Delivery Channel requires a [Configuration Recorder](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const role = new aws.iam.Role("r", {
 *     assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": "sts:AssumeRole",
 *       "Principal": {
 *         "Service": "config.amazonaws.com"
 *       },
 *       "Effect": "Allow",
 *       "Sid": ""
 *     }
 *   ]
 * }
 * `,
 * });
 * const bucket = new aws.s3.Bucket("b", {
 *     forceDestroy: true,
 * });
 * const fooRecorder = new aws.cfg.Recorder("foo", {
 *     roleArn: role.arn,
 * });
 * const fooDeliveryChannel = new aws.cfg.DeliveryChannel("foo", {
 *     s3BucketName: bucket.bucket,
 * }, {dependsOn: [fooRecorder]});
 * const rolePolicy = new aws.iam.RolePolicy("p", {
 *     policy: pulumi.all([bucket.arn, bucket.arn]).apply(([bucketArn, bucketArn1]) => `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "s3:*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": [
 *         "${bucketArn}",
 *         "${bucketArn1}/*"
 *       ]
 *     }
 *   ]
 * }
 * `),
 *     role: role.id,
 * });
 * ```
 */
export class DeliveryChannel extends pulumi.CustomResource {
    /**
     * Get an existing DeliveryChannel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeliveryChannelState, opts?: pulumi.CustomResourceOptions): DeliveryChannel {
        return new DeliveryChannel(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<DeliveryChannelResult> {
        return ctx.list({...args, type: 'aws:cfg/deliveryChannel:DeliveryChannel'});
    }

    /**
     * The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the S3 bucket used to store the configuration history.
     */
    public readonly s3BucketName: pulumi.Output<string>;
    /**
     * The prefix for the specified S3 bucket.
     */
    public readonly s3KeyPrefix: pulumi.Output<string | undefined>;
    /**
     * Options for how AWS Config delivers configuration snapshots. See below
     */
    public readonly snapshotDeliveryProperties: pulumi.Output<{ deliveryFrequency?: string } | undefined>;
    /**
     * The ARN of the SNS topic that AWS Config delivers notifications to.
     */
    public readonly snsTopicArn: pulumi.Output<string | undefined>;

    /**
     * Create a DeliveryChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeliveryChannelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeliveryChannelArgs | DeliveryChannelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DeliveryChannelState = argsOrState as DeliveryChannelState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["s3BucketName"] = state ? state.s3BucketName : undefined;
            inputs["s3KeyPrefix"] = state ? state.s3KeyPrefix : undefined;
            inputs["snapshotDeliveryProperties"] = state ? state.snapshotDeliveryProperties : undefined;
            inputs["snsTopicArn"] = state ? state.snsTopicArn : undefined;
        } else {
            const args = argsOrState as DeliveryChannelArgs | undefined;
            if (!args || args.s3BucketName === undefined) {
                throw new Error("Missing required property 's3BucketName'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["s3BucketName"] = args ? args.s3BucketName : undefined;
            inputs["s3KeyPrefix"] = args ? args.s3KeyPrefix : undefined;
            inputs["snapshotDeliveryProperties"] = args ? args.snapshotDeliveryProperties : undefined;
            inputs["snsTopicArn"] = args ? args.snsTopicArn : undefined;
        }
        super("aws:cfg/deliveryChannel:DeliveryChannel", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DeliveryChannel resources.
 */
export interface DeliveryChannelState {
    /**
     * The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the S3 bucket used to store the configuration history.
     */
    readonly s3BucketName?: pulumi.Input<string>;
    /**
     * The prefix for the specified S3 bucket.
     */
    readonly s3KeyPrefix?: pulumi.Input<string>;
    /**
     * Options for how AWS Config delivers configuration snapshots. See below
     */
    readonly snapshotDeliveryProperties?: pulumi.Input<{ deliveryFrequency?: pulumi.Input<string> }>;
    /**
     * The ARN of the SNS topic that AWS Config delivers notifications to.
     */
    readonly snsTopicArn?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DeliveryChannel resource.
 */
export interface DeliveryChannelArgs {
    /**
     * The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the S3 bucket used to store the configuration history.
     */
    readonly s3BucketName: pulumi.Input<string>;
    /**
     * The prefix for the specified S3 bucket.
     */
    readonly s3KeyPrefix?: pulumi.Input<string>;
    /**
     * Options for how AWS Config delivers configuration snapshots. See below
     */
    readonly snapshotDeliveryProperties?: pulumi.Input<{ deliveryFrequency?: pulumi.Input<string> }>;
    /**
     * The ARN of the SNS topic that AWS Config delivers notifications to.
     */
    readonly snsTopicArn?: pulumi.Input<string>;
}

/**
 * The live DeliveryChannel resource.
 */
export interface DeliveryChannelResult {
    /**
     * The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
     */
    readonly name: string;
    /**
     * The name of the S3 bucket used to store the configuration history.
     */
    readonly s3BucketName: string;
    /**
     * The prefix for the specified S3 bucket.
     */
    readonly s3KeyPrefix?: string;
    /**
     * Options for how AWS Config delivers configuration snapshots. See below
     */
    readonly snapshotDeliveryProperties?: { deliveryFrequency?: string };
    /**
     * The ARN of the SNS topic that AWS Config delivers notifications to.
     */
    readonly snsTopicArn?: string;
}
