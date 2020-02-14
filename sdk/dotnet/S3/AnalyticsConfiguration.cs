// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3
{
    public partial class AnalyticsConfiguration : Pulumi.CustomResource
    {
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        [Output("filter")]
        public Output<Outputs.AnalyticsConfigurationFilter?> Filter { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("storageClassAnalysis")]
        public Output<Outputs.AnalyticsConfigurationStorageClassAnalysis?> StorageClassAnalysis { get; private set; } = null!;


        /// <summary>
        /// Create a AnalyticsConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AnalyticsConfiguration(string name, AnalyticsConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws:s3/analyticsConfiguration:AnalyticsConfiguration", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private AnalyticsConfiguration(string name, Input<string> id, AnalyticsConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("aws:s3/analyticsConfiguration:AnalyticsConfiguration", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AnalyticsConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AnalyticsConfiguration Get(string name, Input<string> id, AnalyticsConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new AnalyticsConfiguration(name, id, state, options);
        }
    }

    public sealed class AnalyticsConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        [Input("filter")]
        public Input<Inputs.AnalyticsConfigurationFilterArgs>? Filter { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("storageClassAnalysis")]
        public Input<Inputs.AnalyticsConfigurationStorageClassAnalysisArgs>? StorageClassAnalysis { get; set; }

        public AnalyticsConfigurationArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationState : Pulumi.ResourceArgs
    {
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        [Input("filter")]
        public Input<Inputs.AnalyticsConfigurationFilterGetArgs>? Filter { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("storageClassAnalysis")]
        public Input<Inputs.AnalyticsConfigurationStorageClassAnalysisGetArgs>? StorageClassAnalysis { get; set; }

        public AnalyticsConfigurationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class AnalyticsConfigurationFilterArgs : Pulumi.ResourceArgs
    {
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public AnalyticsConfigurationFilterArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationFilterGetArgs : Pulumi.ResourceArgs
    {
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public AnalyticsConfigurationFilterGetArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisArgs : Pulumi.ResourceArgs
    {
        [Input("dataExport", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportArgs> DataExport { get; set; } = null!;

        public AnalyticsConfigurationStorageClassAnalysisArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportArgs : Pulumi.ResourceArgs
    {
        [Input("destination", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs> Destination { get; set; } = null!;

        [Input("outputSchemaVersion")]
        public Input<string>? OutputSchemaVersion { get; set; }

        public AnalyticsConfigurationStorageClassAnalysisDataExportArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs : Pulumi.ResourceArgs
    {
        [Input("s3BucketDestination", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs> S3BucketDestination { get; set; } = null!;

        public AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationGetArgs : Pulumi.ResourceArgs
    {
        [Input("s3BucketDestination", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationGetArgs> S3BucketDestination { get; set; } = null!;

        public AnalyticsConfigurationStorageClassAnalysisDataExportDestinationGetArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs : Pulumi.ResourceArgs
    {
        [Input("bucketAccountId")]
        public Input<string>? BucketAccountId { get; set; }

        [Input("bucketArn", required: true)]
        public Input<string> BucketArn { get; set; } = null!;

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationGetArgs : Pulumi.ResourceArgs
    {
        [Input("bucketAccountId")]
        public Input<string>? BucketAccountId { get; set; }

        [Input("bucketArn", required: true)]
        public Input<string> BucketArn { get; set; } = null!;

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationGetArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportGetArgs : Pulumi.ResourceArgs
    {
        [Input("destination", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportDestinationGetArgs> Destination { get; set; } = null!;

        [Input("outputSchemaVersion")]
        public Input<string>? OutputSchemaVersion { get; set; }

        public AnalyticsConfigurationStorageClassAnalysisDataExportGetArgs()
        {
        }
    }

    public sealed class AnalyticsConfigurationStorageClassAnalysisGetArgs : Pulumi.ResourceArgs
    {
        [Input("dataExport", required: true)]
        public Input<AnalyticsConfigurationStorageClassAnalysisDataExportGetArgs> DataExport { get; set; } = null!;

        public AnalyticsConfigurationStorageClassAnalysisGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class AnalyticsConfigurationFilter
    {
        public readonly string? Prefix;
        public readonly ImmutableDictionary<string, object>? Tags;

        [OutputConstructor]
        private AnalyticsConfigurationFilter(
            string? prefix,
            ImmutableDictionary<string, object>? tags)
        {
            Prefix = prefix;
            Tags = tags;
        }
    }

    [OutputType]
    public sealed class AnalyticsConfigurationStorageClassAnalysis
    {
        public readonly AnalyticsConfigurationStorageClassAnalysisDataExport DataExport;

        [OutputConstructor]
        private AnalyticsConfigurationStorageClassAnalysis(AnalyticsConfigurationStorageClassAnalysisDataExport dataExport)
        {
            DataExport = dataExport;
        }
    }

    [OutputType]
    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExport
    {
        public readonly AnalyticsConfigurationStorageClassAnalysisDataExportDestination Destination;
        public readonly string? OutputSchemaVersion;

        [OutputConstructor]
        private AnalyticsConfigurationStorageClassAnalysisDataExport(
            AnalyticsConfigurationStorageClassAnalysisDataExportDestination destination,
            string? outputSchemaVersion)
        {
            Destination = destination;
            OutputSchemaVersion = outputSchemaVersion;
        }
    }

    [OutputType]
    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestination
    {
        public readonly AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination S3BucketDestination;

        [OutputConstructor]
        private AnalyticsConfigurationStorageClassAnalysisDataExportDestination(AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination s3BucketDestination)
        {
            S3BucketDestination = s3BucketDestination;
        }
    }

    [OutputType]
    public sealed class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination
    {
        public readonly string? BucketAccountId;
        public readonly string BucketArn;
        public readonly string? Format;
        public readonly string? Prefix;

        [OutputConstructor]
        private AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(
            string? bucketAccountId,
            string bucketArn,
            string? format,
            string? prefix)
        {
            BucketAccountId = bucketAccountId;
            BucketArn = bucketArn;
            Format = format;
            Prefix = prefix;
        }
    }
    }
}
