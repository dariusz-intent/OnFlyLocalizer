//
//  EventBus.swift
//  OnFlyLocalizer
//
//  Created by Ilja Kosynkin on 2/17/17.
//  Copyright © 2017 Ilja Kosynkin. All rights reserved.
//

import Foundation

public class EventBus {
    private var subscribers: [Int: [WeakReference<Subscriber>]] = [Int: [WeakReference<Subscriber>]]()
    
    public func register(subscriber: Subscriber, forEvent: Int) {
        if subscribers[forEvent] == nil {
            subscribers[forEvent] = [WeakReference<Subscriber>]()
        }
        
        subscribers[forEvent]?.append(WeakReference(value: subscriber))
    }
    
    public func eventFired(eventCode: Int, associatedObject: Any?) {
        guard let references = subscribers[eventCode] else { return }
        
        var actualReferences = [WeakReference<Subscriber>]()
        
        for reference in references {
            if let subscriber = reference.get() {
                subscriber.eventFired(eventCode: eventCode, associatedObject: associatedObject)
                actualReferences.append(reference)
            }
        }
        
        subscribers[eventCode] = actualReferences
    }
}
