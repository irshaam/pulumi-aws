// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Neptune
{
    /// <summary>
    /// A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.
    /// 
    /// You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
    /// meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `instance_class` sizes.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/neptune_cluster_instance.html.markdown.
    /// </summary>
    public partial class ClusterInstance : Pulumi.CustomResource
    {
        /// <summary>
        /// The hostname of the instance. See also `endpoint` and `port`.
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// Specifies whether any instance modifications
        /// are applied immediately, or during the next maintenance window. Default is`false`.
        /// </summary>
        [Output("applyImmediately")]
        public Output<bool> ApplyImmediately { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) of neptune instance
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
        /// </summary>
        [Output("autoMinorVersionUpgrade")]
        public Output<bool?> AutoMinorVersionUpgrade { get; private set; } = null!;

        /// <summary>
        /// The EC2 Availability Zone that the neptune instance is created in.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The identifier of the [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
        /// </summary>
        [Output("clusterIdentifier")]
        public Output<string> ClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The region-unique, immutable identifier for the neptune instance.
        /// </summary>
        [Output("dbiResourceId")]
        public Output<string> DbiResourceId { get; private set; } = null!;

        /// <summary>
        /// The connection endpoint in `address:port` format.
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
        /// </summary>
        [Output("engine")]
        public Output<string?> Engine { get; private set; } = null!;

        /// <summary>
        /// The neptune engine version.
        /// </summary>
        [Output("engineVersion")]
        public Output<string> EngineVersion { get; private set; } = null!;

        /// <summary>
        /// The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.
        /// </summary>
        [Output("identifier")]
        public Output<string> Identifier { get; private set; } = null!;

        /// <summary>
        /// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifier`.
        /// </summary>
        [Output("identifierPrefix")]
        public Output<string> IdentifierPrefix { get; private set; } = null!;

        /// <summary>
        /// The instance class to use.
        /// </summary>
        [Output("instanceClass")]
        public Output<string> InstanceClass { get; private set; } = null!;

        /// <summary>
        /// The ARN for the KMS encryption key if one is set to the neptune cluster.
        /// </summary>
        [Output("kmsKeyArn")]
        public Output<string> KmsKeyArn { get; private set; } = null!;

        /// <summary>
        /// The name of the neptune parameter group to associate with this instance.
        /// </summary>
        [Output("neptuneParameterGroupName")]
        public Output<string?> NeptuneParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
        /// </summary>
        [Output("neptuneSubnetGroupName")]
        public Output<string> NeptuneSubnetGroupName { get; private set; } = null!;

        /// <summary>
        /// The port on which the DB accepts connections. Defaults to `8182`.
        /// </summary>
        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
        /// </summary>
        [Output("preferredBackupWindow")]
        public Output<string> PreferredBackupWindow { get; private set; } = null!;

        /// <summary>
        /// The window to perform maintenance in.
        /// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
        /// </summary>
        [Output("preferredMaintenanceWindow")]
        public Output<string> PreferredMaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
        /// </summary>
        [Output("promotionTier")]
        public Output<int?> PromotionTier { get; private set; } = null!;

        /// <summary>
        /// Bool to control if instance is publicly accessible. Default is `false`.
        /// </summary>
        [Output("publiclyAccessible")]
        public Output<bool?> PubliclyAccessible { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the neptune cluster is encrypted.
        /// </summary>
        [Output("storageEncrypted")]
        public Output<bool> StorageEncrypted { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the instance.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.
        /// </summary>
        [Output("writer")]
        public Output<bool> Writer { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterInstance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterInstance(string name, ClusterInstanceArgs args, CustomResourceOptions? options = null)
            : base("aws:neptune/clusterInstance:ClusterInstance", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ClusterInstance(string name, Input<string> id, ClusterInstanceState? state = null, CustomResourceOptions? options = null)
            : base("aws:neptune/clusterInstance:ClusterInstance", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterInstance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterInstance Get(string name, Input<string> id, ClusterInstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterInstance(name, id, state, options);
        }
    }

    public sealed class ClusterInstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether any instance modifications
        /// are applied immediately, or during the next maintenance window. Default is`false`.
        /// </summary>
        [Input("applyImmediately")]
        public Input<bool>? ApplyImmediately { get; set; }

        /// <summary>
        /// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
        /// </summary>
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        /// <summary>
        /// The EC2 Availability Zone that the neptune instance is created in.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The identifier of the [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
        /// </summary>
        [Input("clusterIdentifier", required: true)]
        public Input<string> ClusterIdentifier { get; set; } = null!;

        /// <summary>
        /// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The neptune engine version.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.
        /// </summary>
        [Input("identifier")]
        public Input<string>? Identifier { get; set; }

        /// <summary>
        /// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifier`.
        /// </summary>
        [Input("identifierPrefix")]
        public Input<string>? IdentifierPrefix { get; set; }

        /// <summary>
        /// The instance class to use.
        /// </summary>
        [Input("instanceClass", required: true)]
        public Input<string> InstanceClass { get; set; } = null!;

        /// <summary>
        /// The name of the neptune parameter group to associate with this instance.
        /// </summary>
        [Input("neptuneParameterGroupName")]
        public Input<string>? NeptuneParameterGroupName { get; set; }

        /// <summary>
        /// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
        /// </summary>
        [Input("neptuneSubnetGroupName")]
        public Input<string>? NeptuneSubnetGroupName { get; set; }

        /// <summary>
        /// The port on which the DB accepts connections. Defaults to `8182`.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
        /// </summary>
        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        /// <summary>
        /// The window to perform maintenance in.
        /// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
        /// </summary>
        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        /// <summary>
        /// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
        /// </summary>
        [Input("promotionTier")]
        public Input<int>? PromotionTier { get; set; }

        /// <summary>
        /// Bool to control if instance is publicly accessible. Default is `false`.
        /// </summary>
        [Input("publiclyAccessible")]
        public Input<bool>? PubliclyAccessible { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ClusterInstanceArgs()
        {
        }
    }

    public sealed class ClusterInstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The hostname of the instance. See also `endpoint` and `port`.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// Specifies whether any instance modifications
        /// are applied immediately, or during the next maintenance window. Default is`false`.
        /// </summary>
        [Input("applyImmediately")]
        public Input<bool>? ApplyImmediately { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of neptune instance
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
        /// </summary>
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        /// <summary>
        /// The EC2 Availability Zone that the neptune instance is created in.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The identifier of the [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
        /// </summary>
        [Input("clusterIdentifier")]
        public Input<string>? ClusterIdentifier { get; set; }

        /// <summary>
        /// The region-unique, immutable identifier for the neptune instance.
        /// </summary>
        [Input("dbiResourceId")]
        public Input<string>? DbiResourceId { get; set; }

        /// <summary>
        /// The connection endpoint in `address:port` format.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The neptune engine version.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// The indentifier for the neptune instance, if omitted, this provider will assign a random, unique identifier.
        /// </summary>
        [Input("identifier")]
        public Input<string>? Identifier { get; set; }

        /// <summary>
        /// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifier`.
        /// </summary>
        [Input("identifierPrefix")]
        public Input<string>? IdentifierPrefix { get; set; }

        /// <summary>
        /// The instance class to use.
        /// </summary>
        [Input("instanceClass")]
        public Input<string>? InstanceClass { get; set; }

        /// <summary>
        /// The ARN for the KMS encryption key if one is set to the neptune cluster.
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        /// <summary>
        /// The name of the neptune parameter group to associate with this instance.
        /// </summary>
        [Input("neptuneParameterGroupName")]
        public Input<string>? NeptuneParameterGroupName { get; set; }

        /// <summary>
        /// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws.neptune.Cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
        /// </summary>
        [Input("neptuneSubnetGroupName")]
        public Input<string>? NeptuneSubnetGroupName { get; set; }

        /// <summary>
        /// The port on which the DB accepts connections. Defaults to `8182`.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
        /// </summary>
        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        /// <summary>
        /// The window to perform maintenance in.
        /// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
        /// </summary>
        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        /// <summary>
        /// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
        /// </summary>
        [Input("promotionTier")]
        public Input<int>? PromotionTier { get; set; }

        /// <summary>
        /// Bool to control if instance is publicly accessible. Default is `false`.
        /// </summary>
        [Input("publiclyAccessible")]
        public Input<bool>? PubliclyAccessible { get; set; }

        /// <summary>
        /// Specifies whether the neptune cluster is encrypted.
        /// </summary>
        [Input("storageEncrypted")]
        public Input<bool>? StorageEncrypted { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.
        /// </summary>
        [Input("writer")]
        public Input<bool>? Writer { get; set; }

        public ClusterInstanceState()
        {
        }
    }
}
