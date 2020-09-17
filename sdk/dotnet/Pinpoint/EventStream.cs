// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Pinpoint
{
    /// <summary>
    /// Provides a Pinpoint Event Stream resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var app = new Aws.Pinpoint.App("app", new Aws.Pinpoint.AppArgs
    ///         {
    ///         });
    ///         var testStream = new Aws.Kinesis.Stream("testStream", new Aws.Kinesis.StreamArgs
    ///         {
    ///             ShardCount = 1,
    ///         });
    ///         var testRole = new Aws.Iam.Role("testRole", new Aws.Iam.RoleArgs
    ///         {
    ///             AssumeRolePolicy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Action"": ""sts:AssumeRole"",
    ///       ""Principal"": {
    ///         ""Service"": ""pinpoint.us-east-1.amazonaws.com""
    ///       },
    ///       ""Effect"": ""Allow"",
    ///       ""Sid"": """"
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         var stream = new Aws.Pinpoint.EventStream("stream", new Aws.Pinpoint.EventStreamArgs
    ///         {
    ///             ApplicationId = app.ApplicationId,
    ///             DestinationStreamArn = testStream.Arn,
    ///             RoleArn = testRole.Arn,
    ///         });
    ///         var testRolePolicy = new Aws.Iam.RolePolicy("testRolePolicy", new Aws.Iam.RolePolicyArgs
    ///         {
    ///             Role = testRole.Id,
    ///             Policy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": {
    ///     ""Action"": [
    ///       ""kinesis:PutRecords"",
    ///       ""kinesis:DescribeStream""
    ///     ],
    ///     ""Effect"": ""Allow"",
    ///     ""Resource"": [
    ///       ""arn:aws:kinesis:us-east-1:*:*/*""
    ///     ]
    ///   }
    /// }
    /// ",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class EventStream : Pulumi.CustomResource
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
        /// </summary>
        [Output("destinationStreamArn")]
        public Output<string> DestinationStreamArn { get; private set; } = null!;

        /// <summary>
        /// The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;


        /// <summary>
        /// Create a EventStream resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EventStream(string name, EventStreamArgs args, CustomResourceOptions? options = null)
            : base("aws:pinpoint/eventStream:EventStream", name, args ?? new EventStreamArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EventStream(string name, Input<string> id, EventStreamState? state = null, CustomResourceOptions? options = null)
            : base("aws:pinpoint/eventStream:EventStream", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing EventStream resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EventStream Get(string name, Input<string> id, EventStreamState? state = null, CustomResourceOptions? options = null)
        {
            return new EventStream(name, id, state, options);
        }
    }

    public sealed class EventStreamArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
        /// </summary>
        [Input("destinationStreamArn", required: true)]
        public Input<string> DestinationStreamArn { get; set; } = null!;

        /// <summary>
        /// The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        public EventStreamArgs()
        {
        }
    }

    public sealed class EventStreamState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
        /// </summary>
        [Input("destinationStreamArn")]
        public Input<string>? DestinationStreamArn { get; set; }

        /// <summary>
        /// The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
        /// </summary>
        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        public EventStreamState()
        {
        }
    }
}
