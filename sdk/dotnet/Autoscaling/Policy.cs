// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AutoScaling
{
    /// <summary>
    /// Provides an AutoScaling Scaling Policy resource.
    /// 
    /// &gt; **NOTE:** You may want to omit `desired_capacity` attribute from attached `aws.autoscaling.Group`
    /// when using autoscaling policies. It's good practice to pick either
    /// [manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
    /// or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
    /// (policy-based) scaling.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown.
    /// </summary>
    public partial class Policy : Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        /// </summary>
        [Output("adjustmentType")]
        public Output<string?> AdjustmentType { get; private set; } = null!;

        /// <summary>
        /// The ARN assigned by AWS to the scaling policy.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The name of the autoscaling group.
        /// </summary>
        [Output("autoscalingGroupName")]
        public Output<string> AutoscalingGroupName { get; private set; } = null!;

        /// <summary>
        /// The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        /// </summary>
        [Output("cooldown")]
        public Output<int?> Cooldown { get; private set; } = null!;

        /// <summary>
        /// The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        /// </summary>
        [Output("estimatedInstanceWarmup")]
        public Output<int?> EstimatedInstanceWarmup { get; private set; } = null!;

        /// <summary>
        /// The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        /// </summary>
        [Output("metricAggregationType")]
        public Output<string> MetricAggregationType { get; private set; } = null!;

        [Output("minAdjustmentMagnitude")]
        public Output<int?> MinAdjustmentMagnitude { get; private set; } = null!;

        /// <summary>
        /// The name of the dimension.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        /// </summary>
        [Output("policyType")]
        public Output<string?> PolicyType { get; private set; } = null!;

        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        [Output("scalingAdjustment")]
        public Output<int?> ScalingAdjustment { get; private set; } = null!;

        /// <summary>
        /// A set of adjustments that manage
        /// group scaling. These have the following structure:
        /// </summary>
        [Output("stepAdjustments")]
        public Output<ImmutableArray<Outputs.PolicyStepAdjustments>> StepAdjustments { get; private set; } = null!;

        /// <summary>
        /// A target tracking policy. These have the following structure:
        /// </summary>
        [Output("targetTrackingConfiguration")]
        public Output<Outputs.PolicyTargetTrackingConfiguration?> TargetTrackingConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs args, CustomResourceOptions? options = null)
            : base("aws:autoscaling/policy:Policy", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
            : base("aws:autoscaling/policy:Policy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, state, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        /// </summary>
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        /// <summary>
        /// The name of the autoscaling group.
        /// </summary>
        [Input("autoscalingGroupName", required: true)]
        public Input<string> AutoscalingGroupName { get; set; } = null!;

        /// <summary>
        /// The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        /// </summary>
        [Input("cooldown")]
        public Input<int>? Cooldown { get; set; }

        /// <summary>
        /// The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        /// </summary>
        [Input("estimatedInstanceWarmup")]
        public Input<int>? EstimatedInstanceWarmup { get; set; }

        /// <summary>
        /// The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        /// </summary>
        [Input("metricAggregationType")]
        public Input<string>? MetricAggregationType { get; set; }

        [Input("minAdjustmentMagnitude")]
        public Input<int>? MinAdjustmentMagnitude { get; set; }

        /// <summary>
        /// The name of the dimension.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        /// </summary>
        [Input("policyType")]
        public Input<string>? PolicyType { get; set; }

        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        [Input("scalingAdjustment")]
        public Input<int>? ScalingAdjustment { get; set; }

        [Input("stepAdjustments")]
        private InputList<Inputs.PolicyStepAdjustmentsArgs>? _stepAdjustments;

        /// <summary>
        /// A set of adjustments that manage
        /// group scaling. These have the following structure:
        /// </summary>
        public InputList<Inputs.PolicyStepAdjustmentsArgs> StepAdjustments
        {
            get => _stepAdjustments ?? (_stepAdjustments = new InputList<Inputs.PolicyStepAdjustmentsArgs>());
            set => _stepAdjustments = value;
        }

        /// <summary>
        /// A target tracking policy. These have the following structure:
        /// </summary>
        [Input("targetTrackingConfiguration")]
        public Input<Inputs.PolicyTargetTrackingConfigurationArgs>? TargetTrackingConfiguration { get; set; }

        public PolicyArgs()
        {
        }
    }

    public sealed class PolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        /// </summary>
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        /// <summary>
        /// The ARN assigned by AWS to the scaling policy.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The name of the autoscaling group.
        /// </summary>
        [Input("autoscalingGroupName")]
        public Input<string>? AutoscalingGroupName { get; set; }

        /// <summary>
        /// The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        /// </summary>
        [Input("cooldown")]
        public Input<int>? Cooldown { get; set; }

        /// <summary>
        /// The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        /// </summary>
        [Input("estimatedInstanceWarmup")]
        public Input<int>? EstimatedInstanceWarmup { get; set; }

        /// <summary>
        /// The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        /// </summary>
        [Input("metricAggregationType")]
        public Input<string>? MetricAggregationType { get; set; }

        [Input("minAdjustmentMagnitude")]
        public Input<int>? MinAdjustmentMagnitude { get; set; }

        /// <summary>
        /// The name of the dimension.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        /// </summary>
        [Input("policyType")]
        public Input<string>? PolicyType { get; set; }

        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        [Input("scalingAdjustment")]
        public Input<int>? ScalingAdjustment { get; set; }

        [Input("stepAdjustments")]
        private InputList<Inputs.PolicyStepAdjustmentsGetArgs>? _stepAdjustments;

        /// <summary>
        /// A set of adjustments that manage
        /// group scaling. These have the following structure:
        /// </summary>
        public InputList<Inputs.PolicyStepAdjustmentsGetArgs> StepAdjustments
        {
            get => _stepAdjustments ?? (_stepAdjustments = new InputList<Inputs.PolicyStepAdjustmentsGetArgs>());
            set => _stepAdjustments = value;
        }

        /// <summary>
        /// A target tracking policy. These have the following structure:
        /// </summary>
        [Input("targetTrackingConfiguration")]
        public Input<Inputs.PolicyTargetTrackingConfigurationGetArgs>? TargetTrackingConfiguration { get; set; }

        public PolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class PolicyStepAdjustmentsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The lower bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity.
        /// </summary>
        [Input("metricIntervalLowerBound")]
        public Input<string>? MetricIntervalLowerBound { get; set; }

        /// <summary>
        /// The upper bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity. The upper bound
        /// must be greater than the lower bound.
        /// </summary>
        [Input("metricIntervalUpperBound")]
        public Input<string>? MetricIntervalUpperBound { get; set; }

        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        [Input("scalingAdjustment", required: true)]
        public Input<int> ScalingAdjustment { get; set; } = null!;

        public PolicyStepAdjustmentsArgs()
        {
        }
    }

    public sealed class PolicyStepAdjustmentsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The lower bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity.
        /// </summary>
        [Input("metricIntervalLowerBound")]
        public Input<string>? MetricIntervalLowerBound { get; set; }

        /// <summary>
        /// The upper bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity. The upper bound
        /// must be greater than the lower bound.
        /// </summary>
        [Input("metricIntervalUpperBound")]
        public Input<string>? MetricIntervalUpperBound { get; set; }

        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        [Input("scalingAdjustment", required: true)]
        public Input<int> ScalingAdjustment { get; set; } = null!;

        public PolicyStepAdjustmentsGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A customized metric. Conflicts with `predefined_metric_specification`.
        /// </summary>
        [Input("customizedMetricSpecification")]
        public Input<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs>? CustomizedMetricSpecification { get; set; }

        /// <summary>
        /// Indicates whether scale in by the target tracking policy is disabled.
        /// </summary>
        [Input("disableScaleIn")]
        public Input<bool>? DisableScaleIn { get; set; }

        /// <summary>
        /// A predefined metric. Conflicts with `customized_metric_specification`.
        /// </summary>
        [Input("predefinedMetricSpecification")]
        public Input<PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs>? PredefinedMetricSpecification { get; set; }

        /// <summary>
        /// The target value for the metric.
        /// </summary>
        [Input("targetValue", required: true)]
        public Input<double> TargetValue { get; set; } = null!;

        public PolicyTargetTrackingConfigurationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs : Pulumi.ResourceArgs
    {
        [Input("metricDimensions")]
        private InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsArgs>? _metricDimensions;

        /// <summary>
        /// The dimensions of the metric.
        /// </summary>
        public InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsArgs> MetricDimensions
        {
            get => _metricDimensions ?? (_metricDimensions = new InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsArgs>());
            set => _metricDimensions = value;
        }

        /// <summary>
        /// The name of the metric.
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The namespace of the metric.
        /// </summary>
        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        /// <summary>
        /// The statistic of the metric.
        /// </summary>
        [Input("statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        /// <summary>
        /// The unit of the metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationGetArgs : Pulumi.ResourceArgs
    {
        [Input("metricDimensions")]
        private InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsGetArgs>? _metricDimensions;

        /// <summary>
        /// The dimensions of the metric.
        /// </summary>
        public InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsGetArgs> MetricDimensions
        {
            get => _metricDimensions ?? (_metricDimensions = new InputList<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsGetArgs>());
            set => _metricDimensions = value;
        }

        /// <summary>
        /// The name of the metric.
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The namespace of the metric.
        /// </summary>
        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        /// <summary>
        /// The statistic of the metric.
        /// </summary>
        [Input("statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        /// <summary>
        /// The unit of the metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public PolicyTargetTrackingConfigurationCustomizedMetricSpecificationGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the dimension.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The value of the dimension.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the dimension.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The value of the dimension.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionsGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A customized metric. Conflicts with `predefined_metric_specification`.
        /// </summary>
        [Input("customizedMetricSpecification")]
        public Input<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationGetArgs>? CustomizedMetricSpecification { get; set; }

        /// <summary>
        /// Indicates whether scale in by the target tracking policy is disabled.
        /// </summary>
        [Input("disableScaleIn")]
        public Input<bool>? DisableScaleIn { get; set; }

        /// <summary>
        /// A predefined metric. Conflicts with `customized_metric_specification`.
        /// </summary>
        [Input("predefinedMetricSpecification")]
        public Input<PolicyTargetTrackingConfigurationPredefinedMetricSpecificationGetArgs>? PredefinedMetricSpecification { get; set; }

        /// <summary>
        /// The target value for the metric.
        /// </summary>
        [Input("targetValue", required: true)]
        public Input<double> TargetValue { get; set; } = null!;

        public PolicyTargetTrackingConfigurationGetArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metric type.
        /// </summary>
        [Input("predefinedMetricType", required: true)]
        public Input<string> PredefinedMetricType { get; set; } = null!;

        /// <summary>
        /// Identifies the resource associated with the metric type.
        /// </summary>
        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        public PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs()
        {
        }
    }

    public sealed class PolicyTargetTrackingConfigurationPredefinedMetricSpecificationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metric type.
        /// </summary>
        [Input("predefinedMetricType", required: true)]
        public Input<string> PredefinedMetricType { get; set; } = null!;

        /// <summary>
        /// Identifies the resource associated with the metric type.
        /// </summary>
        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        public PolicyTargetTrackingConfigurationPredefinedMetricSpecificationGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class PolicyStepAdjustments
    {
        /// <summary>
        /// The lower bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity.
        /// </summary>
        public readonly string? MetricIntervalLowerBound;
        /// <summary>
        /// The upper bound for the
        /// difference between the alarm threshold and the CloudWatch metric.
        /// Without a value, AWS will treat this bound as infinity. The upper bound
        /// must be greater than the lower bound.
        /// </summary>
        public readonly string? MetricIntervalUpperBound;
        /// <summary>
        /// The number of members by which to
        /// scale, when the adjustment bounds are breached. A positive value scales
        /// up. A negative value scales down.
        /// </summary>
        public readonly int ScalingAdjustment;

        [OutputConstructor]
        private PolicyStepAdjustments(
            string? metricIntervalLowerBound,
            string? metricIntervalUpperBound,
            int scalingAdjustment)
        {
            MetricIntervalLowerBound = metricIntervalLowerBound;
            MetricIntervalUpperBound = metricIntervalUpperBound;
            ScalingAdjustment = scalingAdjustment;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingConfiguration
    {
        /// <summary>
        /// A customized metric. Conflicts with `predefined_metric_specification`.
        /// </summary>
        public readonly PolicyTargetTrackingConfigurationCustomizedMetricSpecification? CustomizedMetricSpecification;
        /// <summary>
        /// Indicates whether scale in by the target tracking policy is disabled.
        /// </summary>
        public readonly bool? DisableScaleIn;
        /// <summary>
        /// A predefined metric. Conflicts with `customized_metric_specification`.
        /// </summary>
        public readonly PolicyTargetTrackingConfigurationPredefinedMetricSpecification? PredefinedMetricSpecification;
        /// <summary>
        /// The target value for the metric.
        /// </summary>
        public readonly double TargetValue;

        [OutputConstructor]
        private PolicyTargetTrackingConfiguration(
            PolicyTargetTrackingConfigurationCustomizedMetricSpecification? customizedMetricSpecification,
            bool? disableScaleIn,
            PolicyTargetTrackingConfigurationPredefinedMetricSpecification? predefinedMetricSpecification,
            double targetValue)
        {
            CustomizedMetricSpecification = customizedMetricSpecification;
            DisableScaleIn = disableScaleIn;
            PredefinedMetricSpecification = predefinedMetricSpecification;
            TargetValue = targetValue;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecification
    {
        /// <summary>
        /// The dimensions of the metric.
        /// </summary>
        public readonly ImmutableArray<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensions> MetricDimensions;
        /// <summary>
        /// The name of the metric.
        /// </summary>
        public readonly string MetricName;
        /// <summary>
        /// The namespace of the metric.
        /// </summary>
        public readonly string Namespace;
        /// <summary>
        /// The statistic of the metric.
        /// </summary>
        public readonly string Statistic;
        /// <summary>
        /// The unit of the metric.
        /// </summary>
        public readonly string? Unit;

        [OutputConstructor]
        private PolicyTargetTrackingConfigurationCustomizedMetricSpecification(
            ImmutableArray<PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensions> metricDimensions,
            string metricName,
            string @namespace,
            string statistic,
            string? unit)
        {
            MetricDimensions = metricDimensions;
            MetricName = metricName;
            Namespace = @namespace;
            Statistic = statistic;
            Unit = unit;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensions
    {
        /// <summary>
        /// The name of the dimension.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The value of the dimension.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensions(
            string name,
            string value)
        {
            Name = name;
            Value = value;
        }
    }

    [OutputType]
    public sealed class PolicyTargetTrackingConfigurationPredefinedMetricSpecification
    {
        /// <summary>
        /// The metric type.
        /// </summary>
        public readonly string PredefinedMetricType;
        /// <summary>
        /// Identifies the resource associated with the metric type.
        /// </summary>
        public readonly string? ResourceLabel;

        [OutputConstructor]
        private PolicyTargetTrackingConfigurationPredefinedMetricSpecification(
            string predefinedMetricType,
            string? resourceLabel)
        {
            PredefinedMetricType = predefinedMetricType;
            ResourceLabel = resourceLabel;
        }
    }
    }
}
