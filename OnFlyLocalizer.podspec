Pod::Spec.new do |s|
  s.platform = :ios
  s.ios.deployment_target = '8.0'

  s.name         = "OnFlyLocalizer"
  s.version      = "1.0.2"
  s.summary      = "Lightweight library that simplyfying process of on-the-fly application localization"

  s.description  = <<-DESC
  Usually it's quite hard to implement on-the-fly language change.
  Main purpose of thisl ibrary is too simplify this process by providing scripts for code generation and parsing.
                   DESC

  s.homepage     = "https://github.com/IljaKosynkin/OnFlyLocalizer"

  s.license      = { :type => "Apache License, Version 2.0", :file => "LICENSE" }

  s.author             = { "Ilia Kosynkin" => "ilja.kosynkin@gmail.com" }

  s.source       = { :git => "https://github.com/IljaKosynkin/OnFlyLocalizer.git", :tag => "v1.0.2" }

  s.source_files  = "OnFlyLocalizer", "OnFlyLocalizer/**/*.{h,m,py,swift,sh}"
  s.exclude_files = "Classes/Exclude"
end
