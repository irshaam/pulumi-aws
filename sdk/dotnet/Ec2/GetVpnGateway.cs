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
        /// The VPN Gateway data source provides details about
        /// a specific VPN gateway.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpn_gateway.html.markdown.
        /// </summary>
        public static Task<GetVpnGatewayResult> GetVpnGateway(GetVpnGatewayArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVpnGatewayResult>("aws:ec2/getVpnGateway:getVpnGateway", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetVpnGatewayArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Autonomous System Number (ASN) for the Amazon side of the specific VPN Gateway to retrieve.
        /// </summary>
        [Input("amazonSideAsn")]
        public string? AmazonSideAsn { get; set; }

        /// <summary>
        /// The ID of a VPC attached to the specific VPN Gateway to retrieve.
        /// </summary>
        [Input("attachedVpcId")]
        public string? AttachedVpcId { get; set; }

        /// <summary>
        /// The Availability Zone of the specific VPN Gateway to retrieve.
        /// </summary>
        [Input("availabilityZone")]
        public string? AvailabilityZone { get; set; }

        [Input("filters")]
        private List<Inputs.GetVpnGatewayFiltersArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public List<Inputs.GetVpnGatewayFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetVpnGatewayFiltersArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// The ID of the specific VPN Gateway to retrieve.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The state of the specific VPN Gateway to retrieve.
        /// </summary>
        [Input("state")]
        public string? State { get; set; }

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// A mapping of tags, each pair of which must exactly match
        /// a pair on the desired VPN Gateway.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        public GetVpnGatewayArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetVpnGatewayResult
    {
        public readonly string AmazonSideAsn;
        public readonly string AttachedVpcId;
        public readonly string AvailabilityZone;
        public readonly ImmutableArray<Outputs.GetVpnGatewayFiltersResult> Filters;
        public readonly string Id;
        public readonly string State;
        public readonly ImmutableDictionary<string, object> Tags;

        [OutputConstructor]
        private GetVpnGatewayResult(
            string amazonSideAsn,
            string attachedVpcId,
            string availabilityZone,
            ImmutableArray<Outputs.GetVpnGatewayFiltersResult> filters,
            string id,
            string state,
            ImmutableDictionary<string, object> tags)
        {
            AmazonSideAsn = amazonSideAsn;
            AttachedVpcId = attachedVpcId;
            AvailabilityZone = availabilityZone;
            Filters = filters;
            Id = id;
            State = state;
            Tags = tags;
        }
    }

    namespace Inputs
    {

    public sealed class GetVpnGatewayFiltersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html).
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("values", required: true)]
        private List<string>? _values;

        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A VPN Gateway will be selected if any one of the given values matches.
        /// </summary>
        public List<string> Values
        {
            get => _values ?? (_values = new List<string>());
            set => _values = value;
        }

        public GetVpnGatewayFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetVpnGatewayFiltersResult
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html).
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A VPN Gateway will be selected if any one of the given values matches.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetVpnGatewayFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
