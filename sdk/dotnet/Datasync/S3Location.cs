// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.DataSync
{
    /// <summary>
    /// Manages an S3 Location within AWS DataSync.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown.
    /// </summary>
    public partial class S3Location : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the DataSync Location.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) of the S3 Bucket.
        /// </summary>
        [Output("s3BucketArn")]
        public Output<string> S3BucketArn { get; private set; } = null!;

        /// <summary>
        /// Configuration block containing information for connecting to S3.
        /// </summary>
        [Output("s3Config")]
        public Output<Outputs.S3LocationS3Config> S3Config { get; private set; } = null!;

        /// <summary>
        /// Prefix to perform actions as source or destination.
        /// </summary>
        [Output("subdirectory")]
        public Output<string> Subdirectory { get; private set; } = null!;

        /// <summary>
        /// Key-value pairs of resource tags to assign to the DataSync Location.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        [Output("uri")]
        public Output<string> Uri { get; private set; } = null!;


        /// <summary>
        /// Create a S3Location resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public S3Location(string name, S3LocationArgs args, CustomResourceOptions? options = null)
            : base("aws:datasync/s3Location:S3Location", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private S3Location(string name, Input<string> id, S3LocationState? state = null, CustomResourceOptions? options = null)
            : base("aws:datasync/s3Location:S3Location", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing S3Location resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static S3Location Get(string name, Input<string> id, S3LocationState? state = null, CustomResourceOptions? options = null)
        {
            return new S3Location(name, id, state, options);
        }
    }

    public sealed class S3LocationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the S3 Bucket.
        /// </summary>
        [Input("s3BucketArn", required: true)]
        public Input<string> S3BucketArn { get; set; } = null!;

        /// <summary>
        /// Configuration block containing information for connecting to S3.
        /// </summary>
        [Input("s3Config", required: true)]
        public Input<Inputs.S3LocationS3ConfigArgs> S3Config { get; set; } = null!;

        /// <summary>
        /// Prefix to perform actions as source or destination.
        /// </summary>
        [Input("subdirectory", required: true)]
        public Input<string> Subdirectory { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value pairs of resource tags to assign to the DataSync Location.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public S3LocationArgs()
        {
        }
    }

    public sealed class S3LocationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the DataSync Location.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of the S3 Bucket.
        /// </summary>
        [Input("s3BucketArn")]
        public Input<string>? S3BucketArn { get; set; }

        /// <summary>
        /// Configuration block containing information for connecting to S3.
        /// </summary>
        [Input("s3Config")]
        public Input<Inputs.S3LocationS3ConfigGetArgs>? S3Config { get; set; }

        /// <summary>
        /// Prefix to perform actions as source or destination.
        /// </summary>
        [Input("subdirectory")]
        public Input<string>? Subdirectory { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value pairs of resource tags to assign to the DataSync Location.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public S3LocationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class S3LocationS3ConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.
        /// </summary>
        [Input("bucketAccessRoleArn", required: true)]
        public Input<string> BucketAccessRoleArn { get; set; } = null!;

        public S3LocationS3ConfigArgs()
        {
        }
    }

    public sealed class S3LocationS3ConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.
        /// </summary>
        [Input("bucketAccessRoleArn", required: true)]
        public Input<string> BucketAccessRoleArn { get; set; } = null!;

        public S3LocationS3ConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class S3LocationS3Config
    {
        /// <summary>
        /// Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.
        /// </summary>
        public readonly string BucketAccessRoleArn;

        [OutputConstructor]
        private S3LocationS3Config(string bucketAccessRoleArn)
        {
            BucketAccessRoleArn = bucketAccessRoleArn;
        }
    }
    }
}
