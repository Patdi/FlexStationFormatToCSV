<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FlexStationFormatToCSV</title>
</head>
<body>

  <h1>FlexStationFormatToCSV</h1>

  <p>
    Converts a Molecular Devices FlexStation 3 Microplate Reader <code>.csv</code> file
    to an easier-to-use format.
  </p>

  <hr />

  <h2>Overview</h2>
  <p>
    The output from the Microplate Reader CSV format places each plate in a separate block.
    This script converts that block-based (horizontal) layout into a flat CSV format that is
    easier to analyze in spreadsheets, scripts, or downstream pipelines.
  </p>

  <h3>Example input block format (from FlexStation)</h3>
  <pre><code>Plate: Row13_DMI_t0 1.3
Temperature(C),A1
24.5,-0.004283333
24.5,-0.002208333

~End
Plate: Row13_QoI_t0 1.3
Temperature(C),A1
24.5,0.1707
24.5,0.1259
</code></pre>

  <h3>Converted output format (flat CSV)</h3>
  <p>
    <strong>Example (5-column layout):</strong>
  </p>
  <pre><code>Sample,TimePoint,Well,Coordinate,Absorbance
1,0,A1,0,-0.022333333
2,0,A2,0,-0.031166667
</code></pre>

  <p>
    Column headers:
  </p>
  <pre><code>Sample, TimePoint, Well, Coordinate, Absorbance</code></pre>

  <hr />

  <h2>Usage</h2>

  <h3>Command line</h3>
  <pre><code>cat "your_file".csv | FlexStationFormatToCSV.py &gt; "output".csv</code></pre>

  <p>
    If you use the wildcard <code>*</code>, you can run it on multiple files at once.
  </p>

  <h3>Example (multiple files)</h3>
  <pre><code>cat *.csv | FlexStationFormatToCSV.py &gt; combined_output.csv</code></pre>

  <hr />

  <h2>Files</h2>
  <ul>
    <li><code>FlexStationFormatToCSV.py</code> — conversion script</li>
    <li><code>test_file.csv</code> — expected input format example</li>
    <li><code>test_output.csv</code> — expected output format example</li>
  </ul>

  <hr />

  <h2>Expected Formats</h2>

  <h3>Expected input format in <code>test_file.csv</code></h3>
  <p>
    The input should follow the FlexStation block layout, where each plate appears in its own
    section and ends with <code>~End</code>.
  </p>

  <h3>Expected output format in <code>test_output.csv</code></h3>
  <p>
    The output should be a normalized CSV with one row per sample/well measurement.
  </p>

  <hr />

  <h2>Why did I make this? Why not?</h2>
  <ul>
    <li>Block-based output isn't fun to work with</li>
    <li>This script block-based instrument exports into tabular CSV data</li>
    <li>Makes downstream analysis easier in Python/R/Excel</li>
    <li>Simplifies batch processing of multiple files</li>
  </ul>

</body>
</html>
