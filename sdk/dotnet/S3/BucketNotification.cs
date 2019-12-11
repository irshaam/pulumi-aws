// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3
{
    /// <summary>
    /// Manages a S3 Bucket Notification Configuration. For additional information, see the [Configuring S3 Event Notifications section in the Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).
    /// 
    /// &gt; **NOTE:** S3 Buckets only support a single notification configuration. Declaring multiple `aws.s3.BucketNotification` resources to the same S3 Bucket will cause a perpetual difference in configuration. See the example "Trigger multiple Lambda functions" for an option.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown.
    /// </summary>
    public partial class BucketNotification : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the bucket to put notification configuration.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// Used to configure notifications to a Lambda Function (documented below).
        /// </summary>
        [Output("lambdaFunctions")]
        public Output<ImmutableArray<Outputs.BucketNotificationLambdaFunctions>> LambdaFunctions { get; private set; } = null!;

        /// <summary>
        /// The notification configuration to SQS Queue (documented below).
        /// </summary>
        [Output("queues")]
        public Output<ImmutableArray<Outputs.BucketNotificationQueues>> Queues { get; private set; } = null!;

        /// <summary>
        /// The notification configuration to SNS Topic (documented below).
        /// </summary>
        [Output("topics")]
        public Output<ImmutableArray<Outputs.BucketNotificationTopics>> Topics { get; private set; } = null!;


        /// <summary>
        /// Create a BucketNotification resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BucketNotification(string name, BucketNotificationArgs args, CustomResourceOptions? options = null)
            : base("aws:s3/bucketNotification:BucketNotification", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private BucketNotification(string name, Input<string> id, BucketNotificationState? state = null, CustomResourceOptions? options = null)
            : base("aws:s3/bucketNotification:BucketNotification", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BucketNotification resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BucketNotification Get(string name, Input<string> id, BucketNotificationState? state = null, CustomResourceOptions? options = null)
        {
            return new BucketNotification(name, id, state, options);
        }
    }

    public sealed class BucketNotificationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the bucket to put notification configuration.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        [Input("lambdaFunctions")]
        private InputList<Inputs.BucketNotificationLambdaFunctionsArgs>? _lambdaFunctions;

        /// <summary>
        /// Used to configure notifications to a Lambda Function (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationLambdaFunctionsArgs> LambdaFunctions
        {
            get => _lambdaFunctions ?? (_lambdaFunctions = new InputList<Inputs.BucketNotificationLambdaFunctionsArgs>());
            set => _lambdaFunctions = value;
        }

        [Input("queues")]
        private InputList<Inputs.BucketNotificationQueuesArgs>? _queues;

        /// <summary>
        /// The notification configuration to SQS Queue (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationQueuesArgs> Queues
        {
            get => _queues ?? (_queues = new InputList<Inputs.BucketNotificationQueuesArgs>());
            set => _queues = value;
        }

        [Input("topics")]
        private InputList<Inputs.BucketNotificationTopicsArgs>? _topics;

        /// <summary>
        /// The notification configuration to SNS Topic (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationTopicsArgs> Topics
        {
            get => _topics ?? (_topics = new InputList<Inputs.BucketNotificationTopicsArgs>());
            set => _topics = value;
        }

        public BucketNotificationArgs()
        {
        }
    }

    public sealed class BucketNotificationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the bucket to put notification configuration.
        /// </summary>
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        [Input("lambdaFunctions")]
        private InputList<Inputs.BucketNotificationLambdaFunctionsGetArgs>? _lambdaFunctions;

        /// <summary>
        /// Used to configure notifications to a Lambda Function (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationLambdaFunctionsGetArgs> LambdaFunctions
        {
            get => _lambdaFunctions ?? (_lambdaFunctions = new InputList<Inputs.BucketNotificationLambdaFunctionsGetArgs>());
            set => _lambdaFunctions = value;
        }

        [Input("queues")]
        private InputList<Inputs.BucketNotificationQueuesGetArgs>? _queues;

        /// <summary>
        /// The notification configuration to SQS Queue (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationQueuesGetArgs> Queues
        {
            get => _queues ?? (_queues = new InputList<Inputs.BucketNotificationQueuesGetArgs>());
            set => _queues = value;
        }

        [Input("topics")]
        private InputList<Inputs.BucketNotificationTopicsGetArgs>? _topics;

        /// <summary>
        /// The notification configuration to SNS Topic (documented below).
        /// </summary>
        public InputList<Inputs.BucketNotificationTopicsGetArgs> Topics
        {
            get => _topics ?? (_topics = new InputList<Inputs.BucketNotificationTopicsGetArgs>());
            set => _topics = value;
        }

        public BucketNotificationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class BucketNotificationLambdaFunctionsArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon Lambda function ARN.
        /// </summary>
        [Input("lambdaFunctionArn")]
        public Input<string>? LambdaFunctionArn { get; set; }

        public BucketNotificationLambdaFunctionsArgs()
        {
        }
    }

    public sealed class BucketNotificationLambdaFunctionsGetArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon Lambda function ARN.
        /// </summary>
        [Input("lambdaFunctionArn")]
        public Input<string>? LambdaFunctionArn { get; set; }

        public BucketNotificationLambdaFunctionsGetArgs()
        {
        }
    }

    public sealed class BucketNotificationQueuesArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon SQS queue ARN.
        /// </summary>
        [Input("queueArn", required: true)]
        public Input<string> QueueArn { get; set; } = null!;

        public BucketNotificationQueuesArgs()
        {
        }
    }

    public sealed class BucketNotificationQueuesGetArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon SQS queue ARN.
        /// </summary>
        [Input("queueArn", required: true)]
        public Input<string> QueueArn { get; set; } = null!;

        public BucketNotificationQueuesGetArgs()
        {
        }
    }

    public sealed class BucketNotificationTopicsArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon SNS topic ARN.
        /// </summary>
        [Input("topicArn", required: true)]
        public Input<string> TopicArn { get; set; } = null!;

        public BucketNotificationTopicsArgs()
        {
        }
    }

    public sealed class BucketNotificationTopicsGetArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        [Input("filterPrefix")]
        public Input<string>? FilterPrefix { get; set; }

        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        [Input("filterSuffix")]
        public Input<string>? FilterSuffix { get; set; }

        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies Amazon SNS topic ARN.
        /// </summary>
        [Input("topicArn", required: true)]
        public Input<string> TopicArn { get; set; } = null!;

        public BucketNotificationTopicsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class BucketNotificationLambdaFunctions
    {
        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public readonly ImmutableArray<string> Events;
        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        public readonly string? FilterPrefix;
        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        public readonly string? FilterSuffix;
        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Specifies Amazon Lambda function ARN.
        /// </summary>
        public readonly string? LambdaFunctionArn;

        [OutputConstructor]
        private BucketNotificationLambdaFunctions(
            ImmutableArray<string> events,
            string? filterPrefix,
            string? filterSuffix,
            string id,
            string? lambdaFunctionArn)
        {
            Events = events;
            FilterPrefix = filterPrefix;
            FilterSuffix = filterSuffix;
            Id = id;
            LambdaFunctionArn = lambdaFunctionArn;
        }
    }

    [OutputType]
    public sealed class BucketNotificationQueues
    {
        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public readonly ImmutableArray<string> Events;
        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        public readonly string? FilterPrefix;
        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        public readonly string? FilterSuffix;
        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Specifies Amazon SQS queue ARN.
        /// </summary>
        public readonly string QueueArn;

        [OutputConstructor]
        private BucketNotificationQueues(
            ImmutableArray<string> events,
            string? filterPrefix,
            string? filterSuffix,
            string id,
            string queueArn)
        {
            Events = events;
            FilterPrefix = filterPrefix;
            FilterSuffix = filterSuffix;
            Id = id;
            QueueArn = queueArn;
        }
    }

    [OutputType]
    public sealed class BucketNotificationTopics
    {
        /// <summary>
        /// Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
        /// </summary>
        public readonly ImmutableArray<string> Events;
        /// <summary>
        /// Specifies object key name prefix.
        /// </summary>
        public readonly string? FilterPrefix;
        /// <summary>
        /// Specifies object key name suffix.
        /// </summary>
        public readonly string? FilterSuffix;
        /// <summary>
        /// Specifies unique identifier for each of the notification configurations.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Specifies Amazon SNS topic ARN.
        /// </summary>
        public readonly string TopicArn;

        [OutputConstructor]
        private BucketNotificationTopics(
            ImmutableArray<string> events,
            string? filterPrefix,
            string? filterSuffix,
            string id,
            string topicArn)
        {
            Events = events;
            FilterPrefix = filterPrefix;
            FilterSuffix = filterSuffix;
            Id = id;
            TopicArn = topicArn;
        }
    }
    }
}
