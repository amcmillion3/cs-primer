require 'net/http'
require 'uri'

def memoize(meth)
  original = method(meth)
  cache = {}

  define_method(meth) do |*args, **kwargs, &block|
    key = args
    return cache[key] if cache.key?(key)

    cache[key] = original.call(*args, **kwargs, &block)
  end
end

memoize def fetch(url)
  uri = URI(url)
  Net::HTTP.get(uri)
end

memoize def fib(n)
  return n if n <= 1
  fib(n - 1) + fib(n - 2)
end

puts fib(35)
puts fetch("https://google.com")
