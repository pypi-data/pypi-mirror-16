import boto3.session
import boto3.s3.transfer


class S3Bucket(object):
    def __init__(
            self, s3_region, s3_bucket,
            aws_access_key_id=None, aws_secret_access_key=None):

        session = boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=s3_region)

        self.session = session
        self.s3 = session.client('s3')
        self.bucket = s3_bucket

    def list(self):
        params = {'Bucket': self.bucket}
        resp = self.s3.list_objects_v2(**params)
        return [o['Key'] for o in resp['Contents']]

    def put_object(self, key, filename, callback=None):
        """
        Upload a file to the bucket.
        """
        transfer = boto3.s3.transfer.S3Transfer(self.s3)
        transfer.upload_file(
            filename, self.bucket, key, callback=callback)

    def url(self, key):
        "Generate a URL to GET a key"
        return '%s/%s/%s' % (
            self.s3.meta.endpoint_url, self.bucket, key
        )

    def signed_url(self, key):
        "Generate a signed URL to GET an object"
        params = {'Bucket': self.bucket, 'Key': key}
        url = self.s3.generate_presigned_url(
                'get_object', Params=params)

        return url
