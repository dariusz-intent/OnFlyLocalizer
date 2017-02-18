//
//  Subscriber.swift
//  OnFlyLocalizer
//
//  Created by Ilja Kosynkin on 2/17/17.
//  Copyright © 2017 Ilja Kosynkin. All rights reserved.
//

import Foundation

public class Subscriber {
    public func eventFired(eventCode: Int, associatedObject: Any?) {
        fatalError("Abstract function call")
    }
}
