// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    public static partial class Invokes
    {
        /// <summary>
        /// `aws.ec2.SecurityGroup` provides details about a specific Security Group.
        /// 
        /// This resource can prove useful when a module accepts a Security Group id as
        /// an input variable and needs to, for example, determine the id of the
        /// VPC that the security group belongs to.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_group.html.markdown.
        /// </summary>
        public static Task<GetSecurityGroupResult> GetSecurityGroup(GetSecurityGroupArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecurityGroupResult>("aws:ec2/getSecurityGroup:getSecurityGroup", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetSecurityGroupArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetSecurityGroupFiltersArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public List<Inputs.GetSecurityGroupFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetSecurityGroupFiltersArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// The id of the specific security group to retrieve.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html).
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// A mapping of tags, each pair of which must exactly match
        /// a pair on the desired security group.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        /// <summary>
        /// The id of the VPC that the desired security group belongs to.
        /// </summary>
        [Input("vpcId")]
        public string? VpcId { get; set; }

        public GetSecurityGroupArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetSecurityGroupResult
    {
        /// <summary>
        /// The computed ARN of the security group.
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// The description of the security group.
        /// </summary>
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetSecurityGroupFiltersResult> Filters;
        public readonly string Id;
        public readonly string Name;
        public readonly ImmutableDictionary<string, object> Tags;
        public readonly string VpcId;

        [OutputConstructor]
        private GetSecurityGroupResult(
            string arn,
            string description,
            ImmutableArray<Outputs.GetSecurityGroupFiltersResult> filters,
            string id,
            string name,
            ImmutableDictionary<string, object> tags,
            string vpcId)
        {
            Arn = arn;
            Description = description;
            Filters = filters;
            Id = id;
            Name = name;
            Tags = tags;
            VpcId = vpcId;
        }
    }

    namespace Inputs
    {

    public sealed class GetSecurityGroupFiltersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html).
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("values", required: true)]
        private List<string>? _values;

        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A Security Group will be selected if any one of the given values matches.
        /// </summary>
        public List<string> Values
        {
            get => _values ?? (_values = new List<string>());
            set => _values = value;
        }

        public GetSecurityGroupFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetSecurityGroupFiltersResult
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html).
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A Security Group will be selected if any one of the given values matches.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetSecurityGroupFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
