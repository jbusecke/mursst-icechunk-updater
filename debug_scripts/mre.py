import icechunk as ic
import earthaccess

bucket = 'nasa-eodc-public'
store_name = "MUR-JPL-L4-GLOB-v4.1-virtual-v1-p2"
store_prefix = f"icechunk/{store_name}"

edl = earthaccess.login(strategy='netrc')
assert edl.authenticated
test_creds = edl.get_s3_credentials(daac='PODAAC')
print(test_creds)
storage = ic.s3_storage(bucket=bucket, prefix=store_prefix, from_env=True)
config = ic.RepositoryConfig.default()
config.set_virtual_chunk_container(ic.VirtualChunkContainer("s3", "s3://", ic.s3_store(region="us-west-2")))
v_chunk_credentials = ic.containers_credentials(s3=ic.s3_static_credentials(access_key_id=test_creds['accessKeyId'], secret_access_key=test_creds['secretAccessKey'], session_token=test_creds['sessionToken']))
repo = ic.Repository.open(
    storage=storage,
    config=config,
    virtual_chunk_credentials=v_chunk_credentials
)
print(repo)