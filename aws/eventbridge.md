# Notes

Each region has a default event bus

```
$ aws events list-event-buses
{
    "EventBuses": [
        {
            "Name": "default",
            "Arn": "arn:aws:events:us-east-1:XXXXX:event-bus/default"
        }
    ]
}

```

And there are built-in rules (Maybe or these are legacy)

```
aws events list-rules | jq -r '.Rules[]|[ .Name, .EventPattern] | @csv'
"DO-NOT-DELETE-AmazonInspectorEc2ManagedRule","{""source"": [""aws.ec2""], ""detail-type"": [""EC2 Instance State-change Notification""]}"
"config_events","{""source"":[""aws.config""]}"
"consolelogin","{""detail-type"":[""AWS Console Sign In via CloudTrail""]}"
"ec2_events","{""source"":[""aws.ec2""]}"
"iam_event","{""source"":[""aws.iam""]}"
```

# Blogs
- https://medium.com/serverless-transformation/eventbridge-the-key-component-in-serverless-architectures-e7d4e60fca2d (March 2020)
- https://medium.com/awesome-cloud/aws-difference-between-amazon-eventbridge-and-amazon-sns-comparison-aws-eventbridge-vs-aws-sns-46708bf5313 (March 2022)

# Applications

## Zendesk
- https://aws.amazon.com/blogs/compute/automating-zendesk-with-amazon-eventbridge-and-aws-step-functions/
- https://github.com/aws-samples/amazon-eventbridge-integration-with-zendesk
- https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-zendesk.html
