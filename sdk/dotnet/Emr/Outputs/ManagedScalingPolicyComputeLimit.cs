// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Emr.Outputs
{

    [OutputType]
    public sealed class ManagedScalingPolicyComputeLimit
    {
        /// <summary>
        /// The upper boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
        /// </summary>
        public readonly int MaximumCapacityUnits;
        /// <summary>
        /// The upper boundary of EC2 units for core node type in a cluster. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.
        /// </summary>
        public readonly int? MaximumCoreCapacityUnits;
        /// <summary>
        /// The upper boundary of On-Demand EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot instances.
        /// </summary>
        public readonly int? MaximumOndemandCapacityUnits;
        /// <summary>
        /// The lower boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
        /// </summary>
        public readonly int MinimumCapacityUnits;
        /// <summary>
        /// The unit type used for specifying a managed scaling policy. Valid Values: `InstanceFleetUnits` | `Instances` | `VCPU`
        /// </summary>
        public readonly string UnitType;

        [OutputConstructor]
        private ManagedScalingPolicyComputeLimit(
            int maximumCapacityUnits,

            int? maximumCoreCapacityUnits,

            int? maximumOndemandCapacityUnits,

            int minimumCapacityUnits,

            string unitType)
        {
            MaximumCapacityUnits = maximumCapacityUnits;
            MaximumCoreCapacityUnits = maximumCoreCapacityUnits;
            MaximumOndemandCapacityUnits = maximumOndemandCapacityUnits;
            MinimumCapacityUnits = minimumCapacityUnits;
            UnitType = unitType;
        }
    }
}