import React, { useState } from 'react';
import { useBattery } from 'react-use';
import styled from 'styled-components';

const BatteryContainer = styled.div`
    position: fixed;
    bottom: 20px;
    right: 20px;
    min-width: 200px;
    max-width: 300px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
`;

const BatteryIcon = styled.div`
    width: 50px;
    height: 20px;
    border: 2px solid #333;
    border-radius: 3px;
    position: relative;
    display: inline-block;
    margin-top: 10px;
    margin-bottom: 10px;

    &::after {
        content: '';
        width: 4px;
        height: 10px;
        background: #333;
        position: absolute;
        top: 3px;
        right: -6px;
        border-radius: 1px;
    }
`;

const BatteryLevel = styled.div`
    height: 100%;
    background-color: ${props => (props.level > 0.2 ? '#0f0' : '#f00')};
    width: ${props => props.level * 100}%;
    border-radius: 2px;
`;

const ToggleButton = styled.button`
    background: none;
    border: none;
    color: #007bff;
    cursor: pointer;
    font-size: 14px;
    margin-top: 10px;
`;

const BatteryComponent = () => {
    const battery = useBattery();
    const { isSupported, level, charging, dischargingTime, chargingTime } = battery;
    const [isExpanded, setIsExpanded] = useState(false);

    const toggleExpand = () => {
        setIsExpanded(!isExpanded);
    };

    if (!isSupported) {
        return (
            <BatteryContainer>
                <strong>Battery sensor</strong>: <span>is not supported</span>
            </BatteryContainer>
        );
    }

    return (
        <BatteryContainer>
            <strong>Charge level:</strong> <span>{(level * 100).toFixed(0)}%</span><br />
            <BatteryIcon>
                <BatteryLevel level={level} />
            </BatteryIcon><br />
            {isExpanded && (
                <>
                    <strong>Charging:</strong> <span>{charging ? "On" : "Off"}</span><br />
                    <strong>Charge time:</strong> <span>{chargingTime ? chargingTime : "Charged"}</span><br />
                    <strong>Discharge time:</strong> <span>{dischargingTime ? dischargingTime : "N/A"}</span>
                </>
            )}
            <ToggleButton onClick={toggleExpand}>
                {isExpanded ? 'Wrap' : 'Unwrap'}
            </ToggleButton>
        </BatteryContainer>
    );
}

export default BatteryComponent;