// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Cognito
{
    /// <summary>
    /// Provides a Cognito User Pool Domain resource.
    /// 
    /// ## Example Usage
    /// ### Amazon Cognito domain
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Cognito.UserPool("example", new Aws.Cognito.UserPoolArgs
    ///         {
    ///         });
    ///         var main = new Aws.Cognito.UserPoolDomain("main", new Aws.Cognito.UserPoolDomainArgs
    ///         {
    ///             Domain = "example-domain",
    ///             UserPoolId = example.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Custom Cognito domain
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleUserPool = new Aws.Cognito.UserPool("exampleUserPool", new Aws.Cognito.UserPoolArgs
    ///         {
    ///         });
    ///         var main = new Aws.Cognito.UserPoolDomain("main", new Aws.Cognito.UserPoolDomainArgs
    ///         {
    ///             Domain = "example-domain.example.com",
    ///             CertificateArn = aws_acm_certificate.Cert.Arn,
    ///             UserPoolId = exampleUserPool.Id,
    ///         });
    ///         var exampleZone = Output.Create(Aws.Route53.GetZone.InvokeAsync(new Aws.Route53.GetZoneArgs
    ///         {
    ///             Name = "example.com",
    ///         }));
    ///         var auth_cognito_A = new Aws.Route53.Record("auth-cognito-A", new Aws.Route53.RecordArgs
    ///         {
    ///             Name = main.Domain,
    ///             Type = "A",
    ///             ZoneId = exampleZone.Apply(exampleZone =&gt; exampleZone.ZoneId),
    ///             Aliases = 
    ///             {
    ///                 new Aws.Route53.Inputs.RecordAliasArgs
    ///                 {
    ///                     EvaluateTargetHealth = false,
    ///                     Name = main.CloudfrontDistributionArn,
    ///                     ZoneId = "Z2FDTNDATAQYW2",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class UserPoolDomain : Pulumi.CustomResource
    {
        /// <summary>
        /// The AWS account ID for the user pool owner.
        /// </summary>
        [Output("awsAccountId")]
        public Output<string> AwsAccountId { get; private set; } = null!;

        /// <summary>
        /// The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
        /// </summary>
        [Output("certificateArn")]
        public Output<string?> CertificateArn { get; private set; } = null!;

        /// <summary>
        /// The URL of the CloudFront distribution. This is required to generate the ALIAS `aws.route53.Record`
        /// </summary>
        [Output("cloudfrontDistributionArn")]
        public Output<string> CloudfrontDistributionArn { get; private set; } = null!;

        /// <summary>
        /// The domain string.
        /// </summary>
        [Output("domain")]
        public Output<string> Domain { get; private set; } = null!;

        /// <summary>
        /// The S3 bucket where the static files for this domain are stored.
        /// </summary>
        [Output("s3Bucket")]
        public Output<string> S3Bucket { get; private set; } = null!;

        /// <summary>
        /// The user pool ID.
        /// </summary>
        [Output("userPoolId")]
        public Output<string> UserPoolId { get; private set; } = null!;

        /// <summary>
        /// The app version.
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a UserPoolDomain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UserPoolDomain(string name, UserPoolDomainArgs args, CustomResourceOptions? options = null)
            : base("aws:cognito/userPoolDomain:UserPoolDomain", name, args ?? new UserPoolDomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UserPoolDomain(string name, Input<string> id, UserPoolDomainState? state = null, CustomResourceOptions? options = null)
            : base("aws:cognito/userPoolDomain:UserPoolDomain", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing UserPoolDomain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UserPoolDomain Get(string name, Input<string> id, UserPoolDomainState? state = null, CustomResourceOptions? options = null)
        {
            return new UserPoolDomain(name, id, state, options);
        }
    }

    public sealed class UserPoolDomainArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
        /// </summary>
        [Input("certificateArn")]
        public Input<string>? CertificateArn { get; set; }

        /// <summary>
        /// The domain string.
        /// </summary>
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        /// <summary>
        /// The user pool ID.
        /// </summary>
        [Input("userPoolId", required: true)]
        public Input<string> UserPoolId { get; set; } = null!;

        public UserPoolDomainArgs()
        {
        }
    }

    public sealed class UserPoolDomainState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AWS account ID for the user pool owner.
        /// </summary>
        [Input("awsAccountId")]
        public Input<string>? AwsAccountId { get; set; }

        /// <summary>
        /// The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
        /// </summary>
        [Input("certificateArn")]
        public Input<string>? CertificateArn { get; set; }

        /// <summary>
        /// The URL of the CloudFront distribution. This is required to generate the ALIAS `aws.route53.Record`
        /// </summary>
        [Input("cloudfrontDistributionArn")]
        public Input<string>? CloudfrontDistributionArn { get; set; }

        /// <summary>
        /// The domain string.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// The S3 bucket where the static files for this domain are stored.
        /// </summary>
        [Input("s3Bucket")]
        public Input<string>? S3Bucket { get; set; }

        /// <summary>
        /// The user pool ID.
        /// </summary>
        [Input("userPoolId")]
        public Input<string>? UserPoolId { get; set; }

        /// <summary>
        /// The app version.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public UserPoolDomainState()
        {
        }
    }
}
