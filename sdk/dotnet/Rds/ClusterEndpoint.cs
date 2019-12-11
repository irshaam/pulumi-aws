// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Rds
{
    /// <summary>
    /// Manages a RDS Aurora Cluster Endpoint.
    /// You can refer to the [User Guide][1].
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/rds_cluster_endpoint.html.markdown.
    /// </summary>
    public partial class ClusterEndpoint : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of cluster
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The identifier to use for the new endpoint. This parameter is stored as a lowercase string.
        /// </summary>
        [Output("clusterEndpointIdentifier")]
        public Output<string> ClusterEndpointIdentifier { get; private set; } = null!;

        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Output("clusterIdentifier")]
        public Output<string> ClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The type of the endpoint. One of: READER , ANY .
        /// </summary>
        [Output("customEndpointType")]
        public Output<string> CustomEndpointType { get; private set; } = null!;

        /// <summary>
        /// A custom endpoint for the Aurora cluster
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with `static_members`.
        /// </summary>
        [Output("excludedMembers")]
        public Output<ImmutableArray<string>> ExcludedMembers { get; private set; } = null!;

        /// <summary>
        /// List of DB instance identifiers that are part of the custom endpoint group. Conflicts with `excluded_members`.
        /// </summary>
        [Output("staticMembers")]
        public Output<ImmutableArray<string>> StaticMembers { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterEndpoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterEndpoint(string name, ClusterEndpointArgs args, CustomResourceOptions? options = null)
            : base("aws:rds/clusterEndpoint:ClusterEndpoint", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ClusterEndpoint(string name, Input<string> id, ClusterEndpointState? state = null, CustomResourceOptions? options = null)
            : base("aws:rds/clusterEndpoint:ClusterEndpoint", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterEndpoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterEndpoint Get(string name, Input<string> id, ClusterEndpointState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterEndpoint(name, id, state, options);
        }
    }

    public sealed class ClusterEndpointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identifier to use for the new endpoint. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("clusterEndpointIdentifier", required: true)]
        public Input<string> ClusterEndpointIdentifier { get; set; } = null!;

        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Input("clusterIdentifier", required: true)]
        public Input<string> ClusterIdentifier { get; set; } = null!;

        /// <summary>
        /// The type of the endpoint. One of: READER , ANY .
        /// </summary>
        [Input("customEndpointType", required: true)]
        public Input<string> CustomEndpointType { get; set; } = null!;

        [Input("excludedMembers")]
        private InputList<string>? _excludedMembers;

        /// <summary>
        /// List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with `static_members`.
        /// </summary>
        public InputList<string> ExcludedMembers
        {
            get => _excludedMembers ?? (_excludedMembers = new InputList<string>());
            set => _excludedMembers = value;
        }

        [Input("staticMembers")]
        private InputList<string>? _staticMembers;

        /// <summary>
        /// List of DB instance identifiers that are part of the custom endpoint group. Conflicts with `excluded_members`.
        /// </summary>
        public InputList<string> StaticMembers
        {
            get => _staticMembers ?? (_staticMembers = new InputList<string>());
            set => _staticMembers = value;
        }

        public ClusterEndpointArgs()
        {
        }
    }

    public sealed class ClusterEndpointState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of cluster
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The identifier to use for the new endpoint. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("clusterEndpointIdentifier")]
        public Input<string>? ClusterEndpointIdentifier { get; set; }

        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Input("clusterIdentifier")]
        public Input<string>? ClusterIdentifier { get; set; }

        /// <summary>
        /// The type of the endpoint. One of: READER , ANY .
        /// </summary>
        [Input("customEndpointType")]
        public Input<string>? CustomEndpointType { get; set; }

        /// <summary>
        /// A custom endpoint for the Aurora cluster
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        [Input("excludedMembers")]
        private InputList<string>? _excludedMembers;

        /// <summary>
        /// List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with `static_members`.
        /// </summary>
        public InputList<string> ExcludedMembers
        {
            get => _excludedMembers ?? (_excludedMembers = new InputList<string>());
            set => _excludedMembers = value;
        }

        [Input("staticMembers")]
        private InputList<string>? _staticMembers;

        /// <summary>
        /// List of DB instance identifiers that are part of the custom endpoint group. Conflicts with `excluded_members`.
        /// </summary>
        public InputList<string> StaticMembers
        {
            get => _staticMembers ?? (_staticMembers = new InputList<string>());
            set => _staticMembers = value;
        }

        public ClusterEndpointState()
        {
        }
    }
}
