aws iam create-role \
  --role-name eksClusterRole \
    --assume-role-policy-document file://"cluster-trust-policy.json"


aws iam attach-role-policy \
      --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
        --role-name eksClusterRole
