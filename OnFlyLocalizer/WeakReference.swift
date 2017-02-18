//
//  WeakReference.swift
//  OnFlyLocalizer
//
//  Created by Ilja Kosynkin on 2/18/17.
//  Copyright © 2017 Ilja Kosynkin. All rights reserved.
//

import Foundation

public class WeakReference<T: AnyObject> {
    private weak var reference: T?
    
    public init(value: T) {
        self.reference = value
    }
    
    public func get() -> T? {
        return self.reference
    }
}
