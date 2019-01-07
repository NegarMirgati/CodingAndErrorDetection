function [output] = noise(input)
    for i = 1:length(input)
        r = rand();
        if (r < 0.1)
            input(i) = 1 - input(i);
        end
    end
    output = input;
end

