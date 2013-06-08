# Disable Rake-environment-task framework detection by uncommenting/setting to false
# Warbler.framework_detection = false
Warbler::Config.new do |config|
  config.dirs = %w(views config tmp)
  config.includes = FileList["example.rb"]
  config.gems += ["sinatra", "haml"]
  config.gems -= ["rails"]
  config.gem_dependencies = true
end
