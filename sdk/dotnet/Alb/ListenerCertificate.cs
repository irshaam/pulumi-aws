// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Alb
{
    /// <summary>
    /// Provides a Load Balancer Listener Certificate resource.
    /// 
    /// This resource is for additional certificates and does not replace the default certificate on the listener.
    /// 
    /// &gt; **Note:** `aws.alb.ListenerCertificate` is known as `aws.lb.ListenerCertificate`. The functionality is identical.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/alb_listener_certificate.html.markdown.
    /// </summary>
    public partial class ListenerCertificate : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the certificate to attach to the listener.
        /// </summary>
        [Output("certificateArn")]
        public Output<string> CertificateArn { get; private set; } = null!;

        /// <summary>
        /// The ARN of the listener to which to attach the certificate.
        /// </summary>
        [Output("listenerArn")]
        public Output<string> ListenerArn { get; private set; } = null!;


        /// <summary>
        /// Create a ListenerCertificate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ListenerCertificate(string name, ListenerCertificateArgs args, CustomResourceOptions? options = null)
            : base("aws:alb/listenerCertificate:ListenerCertificate", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ListenerCertificate(string name, Input<string> id, ListenerCertificateState? state = null, CustomResourceOptions? options = null)
            : base("aws:alb/listenerCertificate:ListenerCertificate", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,                Aliases = { new Alias { Type = "aws:applicationloadbalancing/listenerCertificate:ListenerCertificate" } },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ListenerCertificate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ListenerCertificate Get(string name, Input<string> id, ListenerCertificateState? state = null, CustomResourceOptions? options = null)
        {
            return new ListenerCertificate(name, id, state, options);
        }
    }

    public sealed class ListenerCertificateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the certificate to attach to the listener.
        /// </summary>
        [Input("certificateArn", required: true)]
        public Input<string> CertificateArn { get; set; } = null!;

        /// <summary>
        /// The ARN of the listener to which to attach the certificate.
        /// </summary>
        [Input("listenerArn", required: true)]
        public Input<string> ListenerArn { get; set; } = null!;

        public ListenerCertificateArgs()
        {
        }
    }

    public sealed class ListenerCertificateState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the certificate to attach to the listener.
        /// </summary>
        [Input("certificateArn")]
        public Input<string>? CertificateArn { get; set; }

        /// <summary>
        /// The ARN of the listener to which to attach the certificate.
        /// </summary>
        [Input("listenerArn")]
        public Input<string>? ListenerArn { get; set; }

        public ListenerCertificateState()
        {
        }
    }
}
