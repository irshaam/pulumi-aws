// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Topic} from "./topic";

export class TopicSubscription extends pulumi.CustomResource {
    /**
     * Get an existing TopicSubscription resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicSubscriptionState, opts?: pulumi.CustomResourceOptions): TopicSubscription {
        return new TopicSubscription(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:sns/topicSubscription:TopicSubscription';

    /**
     * Returns true if the given object is an instance of TopicSubscription.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TopicSubscription {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TopicSubscription.__pulumiType;
    }

    /**
     * The ARN of the subscription stored as a more user-friendly property
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
     */
    public readonly confirmationTimeoutInMinutes!: pulumi.Output<number | undefined>;
    /**
     * JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
     */
    public readonly deliveryPolicy!: pulumi.Output<string | undefined>;
    /**
     * The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
     */
    public readonly endpoint!: pulumi.Output<string>;
    /**
     * Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
     */
    public readonly endpointAutoConfirms!: pulumi.Output<boolean | undefined>;
    /**
     * JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
     */
    public readonly filterPolicy!: pulumi.Output<string | undefined>;
    /**
     * The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
     */
    public readonly rawMessageDelivery!: pulumi.Output<boolean | undefined>;
    /**
     * The ARN of the SNS topic to subscribe to
     */
    public readonly topic!: pulumi.Output<Topic>;

    /**
     * Create a TopicSubscription resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TopicSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TopicSubscriptionArgs | TopicSubscriptionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TopicSubscriptionState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["confirmationTimeoutInMinutes"] = state ? state.confirmationTimeoutInMinutes : undefined;
            inputs["deliveryPolicy"] = state ? state.deliveryPolicy : undefined;
            inputs["endpoint"] = state ? state.endpoint : undefined;
            inputs["endpointAutoConfirms"] = state ? state.endpointAutoConfirms : undefined;
            inputs["filterPolicy"] = state ? state.filterPolicy : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["rawMessageDelivery"] = state ? state.rawMessageDelivery : undefined;
            inputs["topic"] = state ? state.topic : undefined;
        } else {
            const args = argsOrState as TopicSubscriptionArgs | undefined;
            if (!args || args.endpoint === undefined) {
                throw new Error("Missing required property 'endpoint'");
            }
            if (!args || args.protocol === undefined) {
                throw new Error("Missing required property 'protocol'");
            }
            if (!args || args.topic === undefined) {
                throw new Error("Missing required property 'topic'");
            }
            inputs["confirmationTimeoutInMinutes"] = args ? args.confirmationTimeoutInMinutes : undefined;
            inputs["deliveryPolicy"] = args ? args.deliveryPolicy : undefined;
            inputs["endpoint"] = args ? args.endpoint : undefined;
            inputs["endpointAutoConfirms"] = args ? args.endpointAutoConfirms : undefined;
            inputs["filterPolicy"] = args ? args.filterPolicy : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["rawMessageDelivery"] = args ? args.rawMessageDelivery : undefined;
            inputs["topic"] = args ? args.topic : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super(TopicSubscription.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TopicSubscription resources.
 */
export interface TopicSubscriptionState {
    /**
     * The ARN of the subscription stored as a more user-friendly property
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
     */
    readonly confirmationTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
     */
    readonly deliveryPolicy?: pulumi.Input<string>;
    /**
     * The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
     */
    readonly endpoint?: pulumi.Input<string>;
    /**
     * Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
     */
    readonly endpointAutoConfirms?: pulumi.Input<boolean>;
    /**
     * JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
     */
    readonly filterPolicy?: pulumi.Input<string>;
    /**
     * The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
     */
    readonly rawMessageDelivery?: pulumi.Input<boolean>;
    /**
     * The ARN of the SNS topic to subscribe to
     */
    readonly topic?: pulumi.Input<Topic>;
}

/**
 * The set of arguments for constructing a TopicSubscription resource.
 */
export interface TopicSubscriptionArgs {
    /**
     * Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
     */
    readonly confirmationTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
     */
    readonly deliveryPolicy?: pulumi.Input<string>;
    /**
     * The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
     */
    readonly endpoint: pulumi.Input<string>;
    /**
     * Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
     */
    readonly endpointAutoConfirms?: pulumi.Input<boolean>;
    /**
     * JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
     */
    readonly filterPolicy?: pulumi.Input<string>;
    /**
     * The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).
     */
    readonly protocol: pulumi.Input<string>;
    /**
     * Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
     */
    readonly rawMessageDelivery?: pulumi.Input<boolean>;
    /**
     * The ARN of the SNS topic to subscribe to
     */
    readonly topic: pulumi.Input<Topic>;
}
