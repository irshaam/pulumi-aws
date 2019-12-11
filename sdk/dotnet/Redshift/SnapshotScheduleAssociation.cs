// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.RedShift
{
    public partial class SnapshotScheduleAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Output("clusterIdentifier")]
        public Output<string> ClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The snapshot schedule identifier.
        /// </summary>
        [Output("scheduleIdentifier")]
        public Output<string> ScheduleIdentifier { get; private set; } = null!;


        /// <summary>
        /// Create a SnapshotScheduleAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SnapshotScheduleAssociation(string name, SnapshotScheduleAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private SnapshotScheduleAssociation(string name, Input<string> id, SnapshotScheduleAssociationState? state = null, CustomResourceOptions? options = null)
            : base("aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SnapshotScheduleAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SnapshotScheduleAssociation Get(string name, Input<string> id, SnapshotScheduleAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new SnapshotScheduleAssociation(name, id, state, options);
        }
    }

    public sealed class SnapshotScheduleAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Input("clusterIdentifier", required: true)]
        public Input<string> ClusterIdentifier { get; set; } = null!;

        /// <summary>
        /// The snapshot schedule identifier.
        /// </summary>
        [Input("scheduleIdentifier", required: true)]
        public Input<string> ScheduleIdentifier { get; set; } = null!;

        public SnapshotScheduleAssociationArgs()
        {
        }
    }

    public sealed class SnapshotScheduleAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The cluster identifier.
        /// </summary>
        [Input("clusterIdentifier")]
        public Input<string>? ClusterIdentifier { get; set; }

        /// <summary>
        /// The snapshot schedule identifier.
        /// </summary>
        [Input("scheduleIdentifier")]
        public Input<string>? ScheduleIdentifier { get; set; }

        public SnapshotScheduleAssociationState()
        {
        }
    }
}
