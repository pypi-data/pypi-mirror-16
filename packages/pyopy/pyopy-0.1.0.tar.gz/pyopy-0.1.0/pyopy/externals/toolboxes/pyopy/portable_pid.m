function [pid] = portable_pid()

isOctave = exist('OCTAVE_VERSION', 'builtin') ~= 0;

if isOctave
  pid = getpid;
else
  pid = feature('getpid');
end

end

