import { render, screen, fireEvent } from '@testing-library/react'
import FileInput from '../../src/components/FileInput'

describe('FileInput', () => {
  it('shows default text when no files selected', () => {
    render(<FileInput files={[]} setFiles={() => {}} disabled={false} />)
    expect(screen.getByText(/clique ou arraste/i)).toBeInTheDocument()
  })

  it('shows file count when files are selected', () => {
    const files = [{ name: 'file1.txt' }, { name: 'file2.pdf' }]
    render(<FileInput files={files} setFiles={() => {}} disabled={false} />)
    expect(screen.getByText(/2 arquivo\(s\) selecionado\(s\)/i)).toBeInTheDocument()
  })

  it('calls setFiles on input change', () => {
    const setFiles = vi.fn()
    render(<FileInput files={[]} setFiles={setFiles} disabled={false} />)
    const input = screen.getByLabelText(/clique ou arraste/i)

    const fakeFiles = [{ name: 'test.txt' }]
    fireEvent.change(input, { target: { files: fakeFiles } })

    expect(setFiles).toHaveBeenCalledWith(fakeFiles)
  })

  it('calls setFiles on drop', () => {
    const setFiles = vi.fn()
    render(<FileInput files={[]} setFiles={setFiles} disabled={false} />)
    const dropArea = screen.getByText(/clique ou arraste/i).parentElement

    const fakeFiles = [{ name: 'drop.txt' }]
    fireEvent.drop(dropArea, { dataTransfer: { files: fakeFiles } })

    expect(setFiles).toHaveBeenCalledWith(fakeFiles)
  })

  it('applies disabled styles and disables input', () => {
    render(<FileInput files={[]} setFiles={() => {}} disabled={true} />)
    const input = screen.getByLabelText(/clique ou arraste/i)
    expect(input).toBeDisabled()

    const dropArea = screen.getByText(/clique ou arraste/i).parentElement
    expect(dropArea).toHaveClass('opacity-50 cursor-not-allowed')
  })
})
