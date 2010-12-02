# source: http://projects.stoneship.org/trac/nanoc/wiki/Helpers/SyntaxColoring

require 'coderay'

def code(*args, &block)
  buffer = eval('_erbout', block.binding)
  
  lang = args.first || :ruby
  pos = buffer.length
  block.call(*args)
  data = buffer[pos..-1]
  buffer[pos..-1] = codify(data, lang)
end

def codify(str, lang)
  CodeRay.scan(str, lang).div :line_numbers => :table
end
