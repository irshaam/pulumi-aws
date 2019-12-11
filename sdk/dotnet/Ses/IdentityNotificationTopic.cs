// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ses
{
    /// <summary>
    /// Resource for managing SES Identity Notification Topics
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_identity_notification_topic.html.markdown.
    /// </summary>
    public partial class IdentityNotificationTopic : Pulumi.CustomResource
    {
        /// <summary>
        /// The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).
        /// </summary>
        [Output("identity")]
        public Output<string> Identity { get; private set; } = null!;

        /// <summary>
        /// Whether SES should include original email headers in SNS notifications of this type. *false* by default.
        /// </summary>
        [Output("includeOriginalHeaders")]
        public Output<bool?> IncludeOriginalHeaders { get; private set; } = null!;

        /// <summary>
        /// The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.
        /// </summary>
        [Output("notificationType")]
        public Output<string> NotificationType { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.
        /// </summary>
        [Output("topicArn")]
        public Output<string?> TopicArn { get; private set; } = null!;


        /// <summary>
        /// Create a IdentityNotificationTopic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IdentityNotificationTopic(string name, IdentityNotificationTopicArgs args, CustomResourceOptions? options = null)
            : base("aws:ses/identityNotificationTopic:IdentityNotificationTopic", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private IdentityNotificationTopic(string name, Input<string> id, IdentityNotificationTopicState? state = null, CustomResourceOptions? options = null)
            : base("aws:ses/identityNotificationTopic:IdentityNotificationTopic", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IdentityNotificationTopic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IdentityNotificationTopic Get(string name, Input<string> id, IdentityNotificationTopicState? state = null, CustomResourceOptions? options = null)
        {
            return new IdentityNotificationTopic(name, id, state, options);
        }
    }

    public sealed class IdentityNotificationTopicArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).
        /// </summary>
        [Input("identity", required: true)]
        public Input<string> Identity { get; set; } = null!;

        /// <summary>
        /// Whether SES should include original email headers in SNS notifications of this type. *false* by default.
        /// </summary>
        [Input("includeOriginalHeaders")]
        public Input<bool>? IncludeOriginalHeaders { get; set; }

        /// <summary>
        /// The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.
        /// </summary>
        [Input("notificationType", required: true)]
        public Input<string> NotificationType { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.
        /// </summary>
        [Input("topicArn")]
        public Input<string>? TopicArn { get; set; }

        public IdentityNotificationTopicArgs()
        {
        }
    }

    public sealed class IdentityNotificationTopicState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).
        /// </summary>
        [Input("identity")]
        public Input<string>? Identity { get; set; }

        /// <summary>
        /// Whether SES should include original email headers in SNS notifications of this type. *false* by default.
        /// </summary>
        [Input("includeOriginalHeaders")]
        public Input<bool>? IncludeOriginalHeaders { get; set; }

        /// <summary>
        /// The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.
        /// </summary>
        [Input("notificationType")]
        public Input<string>? NotificationType { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.
        /// </summary>
        [Input("topicArn")]
        public Input<string>? TopicArn { get; set; }

        public IdentityNotificationTopicState()
        {
        }
    }
}
