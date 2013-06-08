require 'rubygems'
require 'bundler'

Bundler.setup(:default)
Bundler.require

get '/' do
  haml :index
end

get '/:name' do |name|
  "hello #{name}"
end
