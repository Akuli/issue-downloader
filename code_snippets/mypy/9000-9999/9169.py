import typing as t

from mypy_boto3.ec2.type_defs import (
    DescribeInstancesResultTypeDef,
    FilterTypeDef,
    InstanceNetworkInterfaceAttachmentTypeDef,
    InstanceNetworkInterfaceTypeDef,
    InstanceStateTypeDef,
    InstanceTypeDef,
    PlacementTypeDef,
    ReservationTypeDef,
    TagTypeDef,
)

x: t.List[DescribeInstancesResultTypeDef] = [
    DescribeInstancesResultTypeDef(
        Reservations=[
            ReservationTypeDef(
                Instances=[
                    InstanceTypeDef(
                        InstanceId="az1-instance1-id1",
                        Placement=PlacementTypeDef(
                            AvailabilityZone="az1",
                        ),
                        State=InstanceStateTypeDef(
                            Name="running",
                        ),
                        NetworkInterfaces=[
                            InstanceNetworkInterfaceTypeDef(
                                Attachment=InstanceNetworkInterfaceAttachmentTypeDef(
                                    DeviceIndex=0,
                                ),
                                NetworkInterfaceId="az1-instance1-nic0-id1",
                                PrivateDnsName="az1-instance1-nic0-dns1",
                                PrivateIpAddress="az1-instance1-nic0-ip1",
                                SourceDestCheck=True,
                            ),
                        ],
                        Tags=[
                            TagTypeDef(
                                Key="Name",
                                Value="az1-instance1",
                            ),
                        ],
                    ),
                ],
            ),
        ],
        NextToken="next-token1",
    ),
    DescribeInstancesResultTypeDef(
        Reservations=[
            ReservationTypeDef(
                Instances=[
                    InstanceTypeDef(
                        InstanceId="az1-instance2-id2",
                        Placement=PlacementTypeDef(
                            AvailabilityZone="az1",
                        ),
                        State=InstanceStateTypeDef(
                            Name="running",
                        ),
                        NetworkInterfaces=[
                            InstanceNetworkInterfaceTypeDef(
                                Attachment=InstanceNetworkInterfaceAttachmentTypeDef(
                                    DeviceIndex=0,
                                ),
                                NetworkInterfaceId="az1-instance2-nic0-id2",
                                PrivateDnsName="az1-instance2-nic0-dns2",
                                PrivateIpAddress="az1-instance2-nic0-ip2",
                                SourceDestCheck=True,
                            ),
                        ],
                        Tags=[
                            TagTypeDef(
                                Key="Name",
                                Value="az1-instance2",
                            ),
                        ],
                    ),
                ],
            ),
        ],
        NextToken="next-token2",
    ),
    DescribeInstancesResultTypeDef(
        Reservations=[
            ReservationTypeDef(
                Instances=[
                    InstanceTypeDef(
                        InstanceId="az2-instance1-id1",
                        Placement=PlacementTypeDef(
                            AvailabilityZone="az2",
                        ),
                        State=InstanceStateTypeDef(
                            Name="running",
                        ),
                        NetworkInterfaces=[
                            InstanceNetworkInterfaceTypeDef(
                                Attachment=InstanceNetworkInterfaceAttachmentTypeDef(
                                    DeviceIndex=0,
                                ),
                                NetworkInterfaceId="az2-instance1-nic0-id1",
                                PrivateDnsName="az2-instance1-nic0-dns1",
                                PrivateIpAddress="az2-instance1-nic0-ip1",
                                SourceDestCheck=True,
                            ),
                        ],
                        Tags=[
                            TagTypeDef(
                                Key="Name",
                                Value="az2-instance1",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
]
