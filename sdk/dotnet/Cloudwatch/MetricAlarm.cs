// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CloudWatch
{
    /// <summary>
    /// Provides a CloudWatch Metric Alarm resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudwatch_metric_alarm.html.markdown.
    /// </summary>
    public partial class MetricAlarm : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.
        /// </summary>
        [Output("actionsEnabled")]
        public Output<bool?> ActionsEnabled { get; private set; } = null!;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        [Output("alarmActions")]
        public Output<ImmutableArray<string>> AlarmActions { get; private set; } = null!;

        /// <summary>
        /// The description for the alarm.
        /// </summary>
        [Output("alarmDescription")]
        public Output<string?> AlarmDescription { get; private set; } = null!;

        /// <summary>
        /// The descriptive name for the alarm. This name must be unique within the user's AWS account
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ARN of the cloudwatch metric alarm.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`. Additionally, the values  `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, and `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.
        /// </summary>
        [Output("comparisonOperator")]
        public Output<string> ComparisonOperator { get; private set; } = null!;

        /// <summary>
        /// The number of datapoints that must be breaching to trigger the alarm.
        /// </summary>
        [Output("datapointsToAlarm")]
        public Output<int?> DatapointsToAlarm { get; private set; } = null!;

        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Output("dimensions")]
        public Output<ImmutableDictionary<string, object>?> Dimensions { get; private set; } = null!;

        /// <summary>
        /// Used only for alarms
        /// based on percentiles. If you specify `ignore`, the alarm state will not
        /// change during periods with too few data points to be statistically significant.
        /// If you specify `evaluate` or omit this parameter, the alarm will always be
        /// evaluated and possibly change state no matter how many data points are available.
        /// The following values are supported: `ignore`, and `evaluate`.
        /// </summary>
        [Output("evaluateLowSampleCountPercentiles")]
        public Output<string> EvaluateLowSampleCountPercentiles { get; private set; } = null!;

        /// <summary>
        /// The number of periods over which data is compared to the specified threshold.
        /// </summary>
        [Output("evaluationPeriods")]
        public Output<int> EvaluationPeriods { get; private set; } = null!;

        /// <summary>
        /// The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        /// </summary>
        [Output("extendedStatistic")]
        public Output<string?> ExtendedStatistic { get; private set; } = null!;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        [Output("insufficientDataActions")]
        public Output<ImmutableArray<string>> InsufficientDataActions { get; private set; } = null!;

        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Output("metricName")]
        public Output<string?> MetricName { get; private set; } = null!;

        /// <summary>
        /// Enables you to create an alarm based on a metric math expression. You may specify at most 20.
        /// </summary>
        [Output("metricQueries")]
        public Output<ImmutableArray<Outputs.MetricAlarmMetricQueries>> MetricQueries { get; private set; } = null!;

        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Output("namespace")]
        public Output<string?> Namespace { get; private set; } = null!;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        [Output("okActions")]
        public Output<ImmutableArray<string>> OkActions { get; private set; } = null!;

        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        [Output("period")]
        public Output<int?> Period { get; private set; } = null!;

        /// <summary>
        /// The statistic to apply to the alarm's associated metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        [Output("statistic")]
        public Output<string?> Statistic { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.
        /// </summary>
        [Output("threshold")]
        public Output<double?> Threshold { get; private set; } = null!;

        /// <summary>
        /// If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
        /// </summary>
        [Output("thresholdMetricId")]
        public Output<string?> ThresholdMetricId { get; private set; } = null!;

        /// <summary>
        /// Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.
        /// </summary>
        [Output("treatMissingData")]
        public Output<string?> TreatMissingData { get; private set; } = null!;

        /// <summary>
        /// The unit for this metric.
        /// </summary>
        [Output("unit")]
        public Output<string?> Unit { get; private set; } = null!;


        /// <summary>
        /// Create a MetricAlarm resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MetricAlarm(string name, MetricAlarmArgs args, CustomResourceOptions? options = null)
            : base("aws:cloudwatch/metricAlarm:MetricAlarm", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private MetricAlarm(string name, Input<string> id, MetricAlarmState? state = null, CustomResourceOptions? options = null)
            : base("aws:cloudwatch/metricAlarm:MetricAlarm", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MetricAlarm resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MetricAlarm Get(string name, Input<string> id, MetricAlarmState? state = null, CustomResourceOptions? options = null)
        {
            return new MetricAlarm(name, id, state, options);
        }
    }

    public sealed class MetricAlarmArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.
        /// </summary>
        [Input("actionsEnabled")]
        public Input<bool>? ActionsEnabled { get; set; }

        [Input("alarmActions")]
        private InputList<string>? _alarmActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> AlarmActions
        {
            get => _alarmActions ?? (_alarmActions = new InputList<string>());
            set => _alarmActions = value;
        }

        /// <summary>
        /// The description for the alarm.
        /// </summary>
        [Input("alarmDescription")]
        public Input<string>? AlarmDescription { get; set; }

        /// <summary>
        /// The descriptive name for the alarm. This name must be unique within the user's AWS account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`. Additionally, the values  `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, and `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.
        /// </summary>
        [Input("comparisonOperator", required: true)]
        public Input<string> ComparisonOperator { get; set; } = null!;

        /// <summary>
        /// The number of datapoints that must be breaching to trigger the alarm.
        /// </summary>
        [Input("datapointsToAlarm")]
        public Input<int>? DatapointsToAlarm { get; set; }

        [Input("dimensions")]
        private InputMap<object>? _dimensions;

        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public InputMap<object> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputMap<object>());
            set => _dimensions = value;
        }

        /// <summary>
        /// Used only for alarms
        /// based on percentiles. If you specify `ignore`, the alarm state will not
        /// change during periods with too few data points to be statistically significant.
        /// If you specify `evaluate` or omit this parameter, the alarm will always be
        /// evaluated and possibly change state no matter how many data points are available.
        /// The following values are supported: `ignore`, and `evaluate`.
        /// </summary>
        [Input("evaluateLowSampleCountPercentiles")]
        public Input<string>? EvaluateLowSampleCountPercentiles { get; set; }

        /// <summary>
        /// The number of periods over which data is compared to the specified threshold.
        /// </summary>
        [Input("evaluationPeriods", required: true)]
        public Input<int> EvaluationPeriods { get; set; } = null!;

        /// <summary>
        /// The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        /// </summary>
        [Input("extendedStatistic")]
        public Input<string>? ExtendedStatistic { get; set; }

        [Input("insufficientDataActions")]
        private InputList<string>? _insufficientDataActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> InsufficientDataActions
        {
            get => _insufficientDataActions ?? (_insufficientDataActions = new InputList<string>());
            set => _insufficientDataActions = value;
        }

        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("metricName")]
        public Input<string>? MetricName { get; set; }

        [Input("metricQueries")]
        private InputList<Inputs.MetricAlarmMetricQueriesArgs>? _metricQueries;

        /// <summary>
        /// Enables you to create an alarm based on a metric math expression. You may specify at most 20.
        /// </summary>
        public InputList<Inputs.MetricAlarmMetricQueriesArgs> MetricQueries
        {
            get => _metricQueries ?? (_metricQueries = new InputList<Inputs.MetricAlarmMetricQueriesArgs>());
            set => _metricQueries = value;
        }

        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("okActions")]
        private InputList<string>? _okActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> OkActions
        {
            get => _okActions ?? (_okActions = new InputList<string>());
            set => _okActions = value;
        }

        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// The statistic to apply to the alarm's associated metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        [Input("statistic")]
        public Input<string>? Statistic { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.
        /// </summary>
        [Input("threshold")]
        public Input<double>? Threshold { get; set; }

        /// <summary>
        /// If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
        /// </summary>
        [Input("thresholdMetricId")]
        public Input<string>? ThresholdMetricId { get; set; }

        /// <summary>
        /// Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.
        /// </summary>
        [Input("treatMissingData")]
        public Input<string>? TreatMissingData { get; set; }

        /// <summary>
        /// The unit for this metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public MetricAlarmArgs()
        {
        }
    }

    public sealed class MetricAlarmState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.
        /// </summary>
        [Input("actionsEnabled")]
        public Input<bool>? ActionsEnabled { get; set; }

        [Input("alarmActions")]
        private InputList<string>? _alarmActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> AlarmActions
        {
            get => _alarmActions ?? (_alarmActions = new InputList<string>());
            set => _alarmActions = value;
        }

        /// <summary>
        /// The description for the alarm.
        /// </summary>
        [Input("alarmDescription")]
        public Input<string>? AlarmDescription { get; set; }

        /// <summary>
        /// The descriptive name for the alarm. This name must be unique within the user's AWS account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ARN of the cloudwatch metric alarm.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`. Additionally, the values  `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, and `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.
        /// </summary>
        [Input("comparisonOperator")]
        public Input<string>? ComparisonOperator { get; set; }

        /// <summary>
        /// The number of datapoints that must be breaching to trigger the alarm.
        /// </summary>
        [Input("datapointsToAlarm")]
        public Input<int>? DatapointsToAlarm { get; set; }

        [Input("dimensions")]
        private InputMap<object>? _dimensions;

        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public InputMap<object> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputMap<object>());
            set => _dimensions = value;
        }

        /// <summary>
        /// Used only for alarms
        /// based on percentiles. If you specify `ignore`, the alarm state will not
        /// change during periods with too few data points to be statistically significant.
        /// If you specify `evaluate` or omit this parameter, the alarm will always be
        /// evaluated and possibly change state no matter how many data points are available.
        /// The following values are supported: `ignore`, and `evaluate`.
        /// </summary>
        [Input("evaluateLowSampleCountPercentiles")]
        public Input<string>? EvaluateLowSampleCountPercentiles { get; set; }

        /// <summary>
        /// The number of periods over which data is compared to the specified threshold.
        /// </summary>
        [Input("evaluationPeriods")]
        public Input<int>? EvaluationPeriods { get; set; }

        /// <summary>
        /// The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        /// </summary>
        [Input("extendedStatistic")]
        public Input<string>? ExtendedStatistic { get; set; }

        [Input("insufficientDataActions")]
        private InputList<string>? _insufficientDataActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> InsufficientDataActions
        {
            get => _insufficientDataActions ?? (_insufficientDataActions = new InputList<string>());
            set => _insufficientDataActions = value;
        }

        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("metricName")]
        public Input<string>? MetricName { get; set; }

        [Input("metricQueries")]
        private InputList<Inputs.MetricAlarmMetricQueriesGetArgs>? _metricQueries;

        /// <summary>
        /// Enables you to create an alarm based on a metric math expression. You may specify at most 20.
        /// </summary>
        public InputList<Inputs.MetricAlarmMetricQueriesGetArgs> MetricQueries
        {
            get => _metricQueries ?? (_metricQueries = new InputList<Inputs.MetricAlarmMetricQueriesGetArgs>());
            set => _metricQueries = value;
        }

        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("okActions")]
        private InputList<string>? _okActions;

        /// <summary>
        /// The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        /// </summary>
        public InputList<string> OkActions
        {
            get => _okActions ?? (_okActions = new InputList<string>());
            set => _okActions = value;
        }

        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// The statistic to apply to the alarm's associated metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        [Input("statistic")]
        public Input<string>? Statistic { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.
        /// </summary>
        [Input("threshold")]
        public Input<double>? Threshold { get; set; }

        /// <summary>
        /// If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
        /// </summary>
        [Input("thresholdMetricId")]
        public Input<string>? ThresholdMetricId { get; set; }

        /// <summary>
        /// Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.
        /// </summary>
        [Input("treatMissingData")]
        public Input<string>? TreatMissingData { get; set; }

        /// <summary>
        /// The unit for this metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public MetricAlarmState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class MetricAlarmMetricQueriesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        /// </summary>
        [Input("expression")]
        public Input<string>? Expression { get; set; }

        /// <summary>
        /// A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        /// </summary>
        [Input("metric")]
        public Input<MetricAlarmMetricQueriesMetricArgs>? Metric { get; set; }

        /// <summary>
        /// Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        /// </summary>
        [Input("returnData")]
        public Input<bool>? ReturnData { get; set; }

        public MetricAlarmMetricQueriesArgs()
        {
        }
    }

    public sealed class MetricAlarmMetricQueriesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        /// </summary>
        [Input("expression")]
        public Input<string>? Expression { get; set; }

        /// <summary>
        /// A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        /// </summary>
        [Input("metric")]
        public Input<MetricAlarmMetricQueriesMetricGetArgs>? Metric { get; set; }

        /// <summary>
        /// Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        /// </summary>
        [Input("returnData")]
        public Input<bool>? ReturnData { get; set; }

        public MetricAlarmMetricQueriesGetArgs()
        {
        }
    }

    public sealed class MetricAlarmMetricQueriesMetricArgs : Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        private InputMap<object>? _dimensions;

        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public InputMap<object> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputMap<object>());
            set => _dimensions = value;
        }

        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        [Input("period", required: true)]
        public Input<int> Period { get; set; } = null!;

        /// <summary>
        /// The statistic to apply to this metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        [Input("stat", required: true)]
        public Input<string> Stat { get; set; } = null!;

        /// <summary>
        /// The unit for this metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public MetricAlarmMetricQueriesMetricArgs()
        {
        }
    }

    public sealed class MetricAlarmMetricQueriesMetricGetArgs : Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        private InputMap<object>? _dimensions;

        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public InputMap<object> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputMap<object>());
            set => _dimensions = value;
        }

        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        [Input("period", required: true)]
        public Input<int> Period { get; set; } = null!;

        /// <summary>
        /// The statistic to apply to this metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        [Input("stat", required: true)]
        public Input<string> Stat { get; set; } = null!;

        /// <summary>
        /// The unit for this metric.
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public MetricAlarmMetricQueriesMetricGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class MetricAlarmMetricQueries
    {
        /// <summary>
        /// The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        /// </summary>
        public readonly string? Expression;
        /// <summary>
        /// A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        /// </summary>
        public readonly string? Label;
        /// <summary>
        /// The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        /// </summary>
        public readonly MetricAlarmMetricQueriesMetric? Metric;
        /// <summary>
        /// Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        /// </summary>
        public readonly bool? ReturnData;

        [OutputConstructor]
        private MetricAlarmMetricQueries(
            string? expression,
            string id,
            string? label,
            MetricAlarmMetricQueriesMetric? metric,
            bool? returnData)
        {
            Expression = expression;
            Id = id;
            Label = label;
            Metric = metric;
            ReturnData = returnData;
        }
    }

    [OutputType]
    public sealed class MetricAlarmMetricQueriesMetric
    {
        /// <summary>
        /// The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Dimensions;
        /// <summary>
        /// The name for this metric.
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public readonly string MetricName;
        /// <summary>
        /// The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        /// See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        /// </summary>
        public readonly string? Namespace;
        /// <summary>
        /// The period in seconds over which the specified `stat` is applied.
        /// </summary>
        public readonly int Period;
        /// <summary>
        /// The statistic to apply to this metric.
        /// Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        /// </summary>
        public readonly string Stat;
        /// <summary>
        /// The unit for this metric.
        /// </summary>
        public readonly string? Unit;

        [OutputConstructor]
        private MetricAlarmMetricQueriesMetric(
            ImmutableDictionary<string, object>? dimensions,
            string metricName,
            string? @namespace,
            int period,
            string stat,
            string? unit)
        {
            Dimensions = dimensions;
            MetricName = metricName;
            Namespace = @namespace;
            Period = period;
            Stat = stat;
            Unit = unit;
        }
    }
    }
}
