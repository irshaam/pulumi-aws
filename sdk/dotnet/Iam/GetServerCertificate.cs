// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Iam
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to lookup information about IAM Server Certificates.
        /// 
        /// ## Import 
        /// 
        /// The import function will read in certificate body, certificate chain (if it exists), id, name, path, and arn. 
        /// It will not retrieve the private key which is not available through the AWS API.   
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown.
        /// </summary>
        public static Task<GetServerCertificateResult> GetServerCertificate(GetServerCertificateArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServerCertificateResult>("aws:iam/getServerCertificate:getServerCertificate", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetServerCertificateArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// sort results by expiration date. returns the certificate with expiration date in furthest in the future.
        /// </summary>
        [Input("latest")]
        public bool? Latest { get; set; }

        /// <summary>
        /// exact name of the cert to lookup
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// prefix of cert to filter by
        /// </summary>
        [Input("namePrefix")]
        public string? NamePrefix { get; set; }

        /// <summary>
        /// prefix of path to filter by
        /// </summary>
        [Input("pathPrefix")]
        public string? PathPrefix { get; set; }

        public GetServerCertificateArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetServerCertificateResult
    {
        public readonly string Arn;
        public readonly string CertificateBody;
        public readonly string CertificateChain;
        public readonly string ExpirationDate;
        public readonly bool? Latest;
        public readonly string Name;
        public readonly string? NamePrefix;
        public readonly string Path;
        public readonly string? PathPrefix;
        public readonly string UploadDate;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServerCertificateResult(
            string arn,
            string certificateBody,
            string certificateChain,
            string expirationDate,
            bool? latest,
            string name,
            string? namePrefix,
            string path,
            string? pathPrefix,
            string uploadDate,
            string id)
        {
            Arn = arn;
            CertificateBody = certificateBody;
            CertificateChain = certificateChain;
            ExpirationDate = expirationDate;
            Latest = latest;
            Name = name;
            NamePrefix = namePrefix;
            Path = path;
            PathPrefix = pathPrefix;
            UploadDate = uploadDate;
            Id = id;
        }
    }
}
