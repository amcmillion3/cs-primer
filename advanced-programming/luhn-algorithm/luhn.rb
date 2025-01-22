  def verify(digits)
    check_digit = digits.slice!(-1).to_i
    digits.reverse!
    digits = digits.split(//)
    sum = 0

    digits.each_with_index do |d, i|
      if i % 2 == 0
        interim_sum = (2 * d.to_i)
        if interim_sum > 9
          interim_sum -= 9
        end
        sum += interim_sum
      else
        sum += d.to_i
      end
    end

    calculated_check_digit = ((10 - (sum % 10)) % 10)

    check_digit == calculated_check_digit
  end

  raise "verify failure" unless verify("17893729974")
  raise "verify failure" if verify("17893729975")
  puts "ok"
