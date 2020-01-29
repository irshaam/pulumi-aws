// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.GlobalAccelerator
{
    /// <summary>
    /// Provides a Global Accelerator accelerator.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/globalaccelerator_accelerator.html.markdown.
    /// </summary>
    public partial class Accelerator : Pulumi.CustomResource
    {
        /// <summary>
        /// The attributes of the accelerator. Fields documented below.
        /// </summary>
        [Output("attributes")]
        public Output<Outputs.AcceleratorAttributes?> Attributes { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The value for the address type must be `IPV4`.
        /// </summary>
        [Output("ipAddressType")]
        public Output<string?> IpAddressType { get; private set; } = null!;

        /// <summary>
        /// IP address set associated with the accelerator.
        /// </summary>
        [Output("ipSets")]
        public Output<ImmutableArray<Outputs.AcceleratorIpSets>> IpSets { get; private set; } = null!;

        /// <summary>
        /// The name of the accelerator.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Accelerator resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Accelerator(string name, AcceleratorArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:globalaccelerator/accelerator:Accelerator", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Accelerator(string name, Input<string> id, AcceleratorState? state = null, CustomResourceOptions? options = null)
            : base("aws:globalaccelerator/accelerator:Accelerator", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Accelerator resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Accelerator Get(string name, Input<string> id, AcceleratorState? state = null, CustomResourceOptions? options = null)
        {
            return new Accelerator(name, id, state, options);
        }
    }

    public sealed class AcceleratorArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The attributes of the accelerator. Fields documented below.
        /// </summary>
        [Input("attributes")]
        public Input<Inputs.AcceleratorAttributesArgs>? Attributes { get; set; }

        /// <summary>
        /// Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The value for the address type must be `IPV4`.
        /// </summary>
        [Input("ipAddressType")]
        public Input<string>? IpAddressType { get; set; }

        /// <summary>
        /// The name of the accelerator.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AcceleratorArgs()
        {
        }
    }

    public sealed class AcceleratorState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The attributes of the accelerator. Fields documented below.
        /// </summary>
        [Input("attributes")]
        public Input<Inputs.AcceleratorAttributesGetArgs>? Attributes { get; set; }

        /// <summary>
        /// Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The value for the address type must be `IPV4`.
        /// </summary>
        [Input("ipAddressType")]
        public Input<string>? IpAddressType { get; set; }

        [Input("ipSets")]
        private InputList<Inputs.AcceleratorIpSetsGetArgs>? _ipSets;

        /// <summary>
        /// IP address set associated with the accelerator.
        /// </summary>
        public InputList<Inputs.AcceleratorIpSetsGetArgs> IpSets
        {
            get => _ipSets ?? (_ipSets = new InputList<Inputs.AcceleratorIpSetsGetArgs>());
            set => _ipSets = value;
        }

        /// <summary>
        /// The name of the accelerator.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AcceleratorState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class AcceleratorAttributesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether flow logs are enabled.
        /// </summary>
        [Input("flowLogsEnabled")]
        public Input<bool>? FlowLogsEnabled { get; set; }

        /// <summary>
        /// The name of the Amazon S3 bucket for the flow logs.
        /// </summary>
        [Input("flowLogsS3Bucket")]
        public Input<string>? FlowLogsS3Bucket { get; set; }

        /// <summary>
        /// The prefix for the location in the Amazon S3 bucket for the flow logs.
        /// </summary>
        [Input("flowLogsS3Prefix")]
        public Input<string>? FlowLogsS3Prefix { get; set; }

        public AcceleratorAttributesArgs()
        {
        }
    }

    public sealed class AcceleratorAttributesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether flow logs are enabled.
        /// </summary>
        [Input("flowLogsEnabled")]
        public Input<bool>? FlowLogsEnabled { get; set; }

        /// <summary>
        /// The name of the Amazon S3 bucket for the flow logs.
        /// </summary>
        [Input("flowLogsS3Bucket")]
        public Input<string>? FlowLogsS3Bucket { get; set; }

        /// <summary>
        /// The prefix for the location in the Amazon S3 bucket for the flow logs.
        /// </summary>
        [Input("flowLogsS3Prefix")]
        public Input<string>? FlowLogsS3Prefix { get; set; }

        public AcceleratorAttributesGetArgs()
        {
        }
    }

    public sealed class AcceleratorIpSetsGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddresses")]
        private InputList<string>? _ipAddresses;

        /// <summary>
        /// The array of IP addresses in the IP address set.
        /// </summary>
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        /// <summary>
        /// The types of IP addresses included in this IP set.
        /// </summary>
        [Input("ipFamily")]
        public Input<string>? IpFamily { get; set; }

        public AcceleratorIpSetsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class AcceleratorAttributes
    {
        /// <summary>
        /// Indicates whether flow logs are enabled.
        /// </summary>
        public readonly bool? FlowLogsEnabled;
        /// <summary>
        /// The name of the Amazon S3 bucket for the flow logs.
        /// </summary>
        public readonly string? FlowLogsS3Bucket;
        /// <summary>
        /// The prefix for the location in the Amazon S3 bucket for the flow logs.
        /// </summary>
        public readonly string? FlowLogsS3Prefix;

        [OutputConstructor]
        private AcceleratorAttributes(
            bool? flowLogsEnabled,
            string? flowLogsS3Bucket,
            string? flowLogsS3Prefix)
        {
            FlowLogsEnabled = flowLogsEnabled;
            FlowLogsS3Bucket = flowLogsS3Bucket;
            FlowLogsS3Prefix = flowLogsS3Prefix;
        }
    }

    [OutputType]
    public sealed class AcceleratorIpSets
    {
        /// <summary>
        /// The array of IP addresses in the IP address set.
        /// </summary>
        public readonly ImmutableArray<string> IpAddresses;
        /// <summary>
        /// The types of IP addresses included in this IP set.
        /// </summary>
        public readonly string IpFamily;

        [OutputConstructor]
        private AcceleratorIpSets(
            ImmutableArray<string> ipAddresses,
            string ipFamily)
        {
            IpAddresses = ipAddresses;
            IpFamily = ipFamily;
        }
    }
    }
}