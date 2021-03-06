// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3.Outputs
{

    [OutputType]
    public sealed class BucketReplicationConfigurationRule
    {
        /// <summary>
        /// Specifies the destination for the rule (documented below).
        /// </summary>
        public readonly Outputs.BucketReplicationConfigurationRuleDestination Destination;
        /// <summary>
        /// Filter that identifies subset of objects to which the replication rule applies (documented below).
        /// </summary>
        public readonly Outputs.BucketReplicationConfigurationRuleFilter? Filter;
        /// <summary>
        /// Unique identifier for the rule. Must be less than or equal to 255 characters in length.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Object keyname prefix identifying one or more objects to which the rule applies. Must be less than or equal to 1024 characters in length.
        /// </summary>
        public readonly string? Prefix;
        /// <summary>
        /// is optional (with a default value of `0`) but must be unique between multiple rules
        /// </summary>
        public readonly int? Priority;
        /// <summary>
        /// Specifies special object selection criteria (documented below).
        /// </summary>
        public readonly Outputs.BucketReplicationConfigurationRuleSourceSelectionCriteria? SourceSelectionCriteria;
        /// <summary>
        /// The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private BucketReplicationConfigurationRule(
            Outputs.BucketReplicationConfigurationRuleDestination destination,

            Outputs.BucketReplicationConfigurationRuleFilter? filter,

            string? id,

            string? prefix,

            int? priority,

            Outputs.BucketReplicationConfigurationRuleSourceSelectionCriteria? sourceSelectionCriteria,

            string status)
        {
            Destination = destination;
            Filter = filter;
            Id = id;
            Prefix = prefix;
            Priority = priority;
            SourceSelectionCriteria = sourceSelectionCriteria;
            Status = status;
        }
    }
}
