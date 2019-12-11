// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Dlm
{
    /// <summary>
    /// Provides a [Data Lifecycle Manager (DLM) lifecycle policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) for managing snapshots.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dlm_lifecycle_policy.html.markdown.
    /// </summary>
    public partial class LifecyclePolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the DLM Lifecycle Policy.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description for the DLM lifecycle policy.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The ARN of an IAM role that is able to be assumed by the DLM service.
        /// </summary>
        [Output("executionRoleArn")]
        public Output<string> ExecutionRoleArn { get; private set; } = null!;

        /// <summary>
        /// See the `policy_details` configuration block. Max of 1.
        /// </summary>
        [Output("policyDetails")]
        public Output<Outputs.LifecyclePolicyPolicyDetails> PolicyDetails { get; private set; } = null!;

        /// <summary>
        /// Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.
        /// </summary>
        [Output("state")]
        public Output<string?> State { get; private set; } = null!;

        /// <summary>
        /// Key-value mapping of resource tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a LifecyclePolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LifecyclePolicy(string name, LifecyclePolicyArgs args, CustomResourceOptions? options = null)
            : base("aws:dlm/lifecyclePolicy:LifecyclePolicy", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private LifecyclePolicy(string name, Input<string> id, LifecyclePolicyState? state = null, CustomResourceOptions? options = null)
            : base("aws:dlm/lifecyclePolicy:LifecyclePolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LifecyclePolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LifecyclePolicy Get(string name, Input<string> id, LifecyclePolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new LifecyclePolicy(name, id, state, options);
        }
    }

    public sealed class LifecyclePolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description for the DLM lifecycle policy.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The ARN of an IAM role that is able to be assumed by the DLM service.
        /// </summary>
        [Input("executionRoleArn", required: true)]
        public Input<string> ExecutionRoleArn { get; set; } = null!;

        /// <summary>
        /// See the `policy_details` configuration block. Max of 1.
        /// </summary>
        [Input("policyDetails", required: true)]
        public Input<Inputs.LifecyclePolicyPolicyDetailsArgs> PolicyDetails { get; set; } = null!;

        /// <summary>
        /// Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public LifecyclePolicyArgs()
        {
        }
    }

    public sealed class LifecyclePolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the DLM Lifecycle Policy.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// A description for the DLM lifecycle policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ARN of an IAM role that is able to be assumed by the DLM service.
        /// </summary>
        [Input("executionRoleArn")]
        public Input<string>? ExecutionRoleArn { get; set; }

        /// <summary>
        /// See the `policy_details` configuration block. Max of 1.
        /// </summary>
        [Input("policyDetails")]
        public Input<Inputs.LifecyclePolicyPolicyDetailsGetArgs>? PolicyDetails { get; set; }

        /// <summary>
        /// Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public LifecyclePolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class LifecyclePolicyPolicyDetailsArgs : Pulumi.ResourceArgs
    {
        [Input("resourceTypes", required: true)]
        private InputList<string>? _resourceTypes;

        /// <summary>
        /// A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
        /// </summary>
        public InputList<string> ResourceTypes
        {
            get => _resourceTypes ?? (_resourceTypes = new InputList<string>());
            set => _resourceTypes = value;
        }

        [Input("schedules", required: true)]
        private InputList<LifecyclePolicyPolicyDetailsSchedulesArgs>? _schedules;

        /// <summary>
        /// See the `schedule` configuration block.
        /// </summary>
        public InputList<LifecyclePolicyPolicyDetailsSchedulesArgs> Schedules
        {
            get => _schedules ?? (_schedules = new InputList<LifecyclePolicyPolicyDetailsSchedulesArgs>());
            set => _schedules = value;
        }

        [Input("targetTags", required: true)]
        private InputMap<object>? _targetTags;

        /// <summary>
        /// A mapping of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
        /// </summary>
        public InputMap<object> TargetTags
        {
            get => _targetTags ?? (_targetTags = new InputMap<object>());
            set => _targetTags = value;
        }

        public LifecyclePolicyPolicyDetailsArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsGetArgs : Pulumi.ResourceArgs
    {
        [Input("resourceTypes", required: true)]
        private InputList<string>? _resourceTypes;

        /// <summary>
        /// A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
        /// </summary>
        public InputList<string> ResourceTypes
        {
            get => _resourceTypes ?? (_resourceTypes = new InputList<string>());
            set => _resourceTypes = value;
        }

        [Input("schedules", required: true)]
        private InputList<LifecyclePolicyPolicyDetailsSchedulesGetArgs>? _schedules;

        /// <summary>
        /// See the `schedule` configuration block.
        /// </summary>
        public InputList<LifecyclePolicyPolicyDetailsSchedulesGetArgs> Schedules
        {
            get => _schedules ?? (_schedules = new InputList<LifecyclePolicyPolicyDetailsSchedulesGetArgs>());
            set => _schedules = value;
        }

        [Input("targetTags", required: true)]
        private InputMap<object>? _targetTags;

        /// <summary>
        /// A mapping of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
        /// </summary>
        public InputMap<object> TargetTags
        {
            get => _targetTags ?? (_targetTags = new InputMap<object>());
            set => _targetTags = value;
        }

        public LifecyclePolicyPolicyDetailsGetArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
        /// </summary>
        [Input("copyTags")]
        public Input<bool>? CopyTags { get; set; }

        /// <summary>
        /// See the `create_rule` block. Max of 1 per schedule.
        /// </summary>
        [Input("createRule", required: true)]
        public Input<LifecyclePolicyPolicyDetailsSchedulesCreateRuleArgs> CreateRule { get; set; } = null!;

        /// <summary>
        /// A name for the schedule.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// See the `retain_rule` block. Max of 1 per schedule.
        /// </summary>
        [Input("retainRule", required: true)]
        public Input<LifecyclePolicyPolicyDetailsSchedulesRetainRuleArgs> RetainRule { get; set; } = null!;

        [Input("tagsToAdd")]
        private InputMap<object>? _tagsToAdd;

        /// <summary>
        /// A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
        /// </summary>
        public InputMap<object> TagsToAdd
        {
            get => _tagsToAdd ?? (_tagsToAdd = new InputMap<object>());
            set => _tagsToAdd = value;
        }

        public LifecyclePolicyPolicyDetailsSchedulesArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesCreateRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// How often this lifecycle policy should be evaluated. `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
        /// </summary>
        [Input("interval", required: true)]
        public Input<int> Interval { get; set; } = null!;

        /// <summary>
        /// The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
        /// </summary>
        [Input("intervalUnit")]
        public Input<string>? IntervalUnit { get; set; }

        /// <summary>
        /// A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
        /// </summary>
        [Input("times")]
        public Input<string>? Times { get; set; }

        public LifecyclePolicyPolicyDetailsSchedulesCreateRuleArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesCreateRuleGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// How often this lifecycle policy should be evaluated. `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
        /// </summary>
        [Input("interval", required: true)]
        public Input<int> Interval { get; set; } = null!;

        /// <summary>
        /// The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
        /// </summary>
        [Input("intervalUnit")]
        public Input<string>? IntervalUnit { get; set; }

        /// <summary>
        /// A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
        /// </summary>
        [Input("times")]
        public Input<string>? Times { get; set; }

        public LifecyclePolicyPolicyDetailsSchedulesCreateRuleGetArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
        /// </summary>
        [Input("copyTags")]
        public Input<bool>? CopyTags { get; set; }

        /// <summary>
        /// See the `create_rule` block. Max of 1 per schedule.
        /// </summary>
        [Input("createRule", required: true)]
        public Input<LifecyclePolicyPolicyDetailsSchedulesCreateRuleGetArgs> CreateRule { get; set; } = null!;

        /// <summary>
        /// A name for the schedule.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// See the `retain_rule` block. Max of 1 per schedule.
        /// </summary>
        [Input("retainRule", required: true)]
        public Input<LifecyclePolicyPolicyDetailsSchedulesRetainRuleGetArgs> RetainRule { get; set; } = null!;

        [Input("tagsToAdd")]
        private InputMap<object>? _tagsToAdd;

        /// <summary>
        /// A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
        /// </summary>
        public InputMap<object> TagsToAdd
        {
            get => _tagsToAdd ?? (_tagsToAdd = new InputMap<object>());
            set => _tagsToAdd = value;
        }

        public LifecyclePolicyPolicyDetailsSchedulesGetArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesRetainRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// How many snapshots to keep. Must be an integer between 1 and 1000.
        /// </summary>
        [Input("count", required: true)]
        public Input<int> Count { get; set; } = null!;

        public LifecyclePolicyPolicyDetailsSchedulesRetainRuleArgs()
        {
        }
    }

    public sealed class LifecyclePolicyPolicyDetailsSchedulesRetainRuleGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// How many snapshots to keep. Must be an integer between 1 and 1000.
        /// </summary>
        [Input("count", required: true)]
        public Input<int> Count { get; set; } = null!;

        public LifecyclePolicyPolicyDetailsSchedulesRetainRuleGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class LifecyclePolicyPolicyDetails
    {
        /// <summary>
        /// A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
        /// </summary>
        public readonly ImmutableArray<string> ResourceTypes;
        /// <summary>
        /// See the `schedule` configuration block.
        /// </summary>
        public readonly ImmutableArray<LifecyclePolicyPolicyDetailsSchedules> Schedules;
        /// <summary>
        /// A mapping of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
        /// </summary>
        public readonly ImmutableDictionary<string, object> TargetTags;

        [OutputConstructor]
        private LifecyclePolicyPolicyDetails(
            ImmutableArray<string> resourceTypes,
            ImmutableArray<LifecyclePolicyPolicyDetailsSchedules> schedules,
            ImmutableDictionary<string, object> targetTags)
        {
            ResourceTypes = resourceTypes;
            Schedules = schedules;
            TargetTags = targetTags;
        }
    }

    [OutputType]
    public sealed class LifecyclePolicyPolicyDetailsSchedules
    {
        /// <summary>
        /// Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
        /// </summary>
        public readonly bool CopyTags;
        /// <summary>
        /// See the `create_rule` block. Max of 1 per schedule.
        /// </summary>
        public readonly LifecyclePolicyPolicyDetailsSchedulesCreateRule CreateRule;
        /// <summary>
        /// A name for the schedule.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// See the `retain_rule` block. Max of 1 per schedule.
        /// </summary>
        public readonly LifecyclePolicyPolicyDetailsSchedulesRetainRule RetainRule;
        /// <summary>
        /// A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? TagsToAdd;

        [OutputConstructor]
        private LifecyclePolicyPolicyDetailsSchedules(
            bool copyTags,
            LifecyclePolicyPolicyDetailsSchedulesCreateRule createRule,
            string name,
            LifecyclePolicyPolicyDetailsSchedulesRetainRule retainRule,
            ImmutableDictionary<string, object>? tagsToAdd)
        {
            CopyTags = copyTags;
            CreateRule = createRule;
            Name = name;
            RetainRule = retainRule;
            TagsToAdd = tagsToAdd;
        }
    }

    [OutputType]
    public sealed class LifecyclePolicyPolicyDetailsSchedulesCreateRule
    {
        /// <summary>
        /// How often this lifecycle policy should be evaluated. `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
        /// </summary>
        public readonly int Interval;
        /// <summary>
        /// The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
        /// </summary>
        public readonly string? IntervalUnit;
        /// <summary>
        /// A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
        /// </summary>
        public readonly string Times;

        [OutputConstructor]
        private LifecyclePolicyPolicyDetailsSchedulesCreateRule(
            int interval,
            string? intervalUnit,
            string times)
        {
            Interval = interval;
            IntervalUnit = intervalUnit;
            Times = times;
        }
    }

    [OutputType]
    public sealed class LifecyclePolicyPolicyDetailsSchedulesRetainRule
    {
        /// <summary>
        /// How many snapshots to keep. Must be an integer between 1 and 1000.
        /// </summary>
        public readonly int Count;

        [OutputConstructor]
        private LifecyclePolicyPolicyDetailsSchedulesRetainRule(int count)
        {
            Count = count;
        }
    }
    }
}
